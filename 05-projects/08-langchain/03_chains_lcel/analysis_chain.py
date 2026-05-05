# -*- coding: utf-8 -*-
"""
文档分析管道核心模块
"""

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableLambda

from config import API_KEY, API_URL, MODEL_NAME, TEMPERATURE
from prompts import SUMMARY_PROMPT, KEYWORDS_PROMPT, SENTIMENT_PROMPT, REPORT_PROMPT


class DocumentAnalyzer:
    """文档分析器"""
    
    def __init__(self):
        # 初始化 LLM
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            api_key=API_KEY,
            base_url=API_URL,
            temperature=TEMPERATURE,
        )
        
        # 构建分析链
        self._build_chains()
    
    def _build_chains(self):
        """构建分析链"""
        # 摘要链
        self.summary_chain = SUMMARY_PROMPT | self.llm | StrOutputParser()
        
        # 关键词链
        self.keywords_chain = KEYWORDS_PROMPT | self.llm | StrOutputParser()
        
        # 情感链
        self.sentiment_chain = SENTIMENT_PROMPT | self.llm | StrOutputParser()
        
        # 并行分析链
        self.analysis_parallel = RunnableParallel(
            summary=self.summary_chain,
            keywords=self.keywords_chain,
            sentiment=self.sentiment_chain
        )
        
        # 报告生成链
        self.report_chain = REPORT_PROMPT | self.llm | StrOutputParser()
        
        # 完整管道
        self.full_chain = self.analysis_parallel | self.report_chain
    
    def analyze(self, text: str) -> dict:
        """
        分析文本
        
        Args:
            text: 待分析文本
        
        Returns:
            包含分析结果的字典
        """
        # 并行执行分析
        analysis_result = self.analysis_parallel.invoke({"text": text})
        
        # 生成报告
        report = self.report_chain.invoke(analysis_result)
        
        return {
            "summary": analysis_result["summary"],
            "keywords": analysis_result["keywords"],
            "sentiment": analysis_result["sentiment"],
            "report": report
        }
    
    def analyze_stream(self, text: str):
        """
        流式分析文本
        
        Args:
            text: 待分析文本
        
        Yields:
            分析结果片段
        """
        # 先并行分析
        analysis_result = self.analysis_parallel.invoke({"text": text})
        
        # 流式生成报告
        for chunk in self.report_chain.stream(analysis_result):
            yield chunk
    
    def batch_analyze(self, texts: list) -> list:
        """
        批量分析文本
        
        Args:
            texts: 待分析文本列表
        
        Returns:
            分析结果列表
        """
        inputs = [{"text": text} for text in texts]
        results = self.analysis_parallel.batch(inputs)
        
        reports = []
        for result in results:
            report = self.report_chain.invoke(result)
            reports.append({
                "summary": result["summary"],
                "keywords": result["keywords"],
                "sentiment": result["sentiment"],
                "report": report
            })
        
        return reports
