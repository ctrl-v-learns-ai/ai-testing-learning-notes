# -*- coding: utf-8 -*-
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE, TOP_K
from document_store import DocumentStore


class RAGChain:
    def __init__(self):
        self.doc_store = DocumentStore()

        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )

        self.rag_prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer based on the context below. If no context, say you dont know.\n\nContext: {context}"),
            MessagesPlaceholder(variable_name="history"),
            ("human", "{input}")
        ])

        self.store = {}

        def get_session_history(session_id):
            if session_id not in self.store:
                self.store[session_id] = InMemoryChatMessageHistory()
            return self.store[session_id]

        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        retriever = self.doc_store.get_retriever(TOP_K)

        chain = (
            {"context": retriever | format_docs, "input": RunnablePassthrough(), "history": lambda x: []}
            | self.rag_prompt
            | self.llm
            | StrOutputParser()
        )

        self.chain = RunnableWithMessageHistory(
            chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="history"
        )

    def chat(self, user_input: str, session_id: str = "default") -> str:
        config = {"configurable": {"session_id": session_id}}
        return self.chain.invoke({"input": user_input}, config=config)

    def chat_stream(self, user_input: str, session_id: str = "default"):
        config = {"configurable": {"session_id": session_id}}
        for chunk in self.chain.stream({"input": user_input}, config=config):
            yield chunk

    def add_document(self, file_path: str) -> int:
        return self.doc_store.add_document(file_path)
