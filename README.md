# RakshitChaurasia-langsmith-MAT496
This repository will include each and every detail of what I have learned and self reflected throughout my journey of learning  Langsmith from basic .
Lesson 1

Learning Summary from the Video of Lesson 1
Learned to use LangSmith Python SDK for tracing, including setting environment variables, applying the traceable decorator to functions, and utilizing metadata annotation to enrich trace data. The updated file introduces a dummy retriever example for simulating vector DB retrieval and demonstrates runtime metadata usage.

Set up environment variables for LangSmith and OpenAI
What was learned in this process ?

=> How to correctly configure environment variables required to enable LangSmith tracing and OpenAI API access.

=> Importance of setting LANGSMITH_TRACING and project keys for the LangSmith SDK to function.

Implemented function tracing with traceable decorator
What was learned in this process ?

=> How to use the traceable decorator from LangSmith SDK to log function calls, capture inputs, outputs, and errors automatically.

=> How the decorator creates a trace run tree supporting asynchronous background logging without blocking main execution.

Added and used a dummy vector database retriever for tracing demos
What was learned in this process ?

=> How to simulate a vector DB retriever for Retrieval-Augmented Generation (RAG) pipelines using a simple dummy class for testing.

=> How such a retriever integrates within tracing to demonstrate end-to-end observability of data retrieval steps.

 Incorporated metadata annotations and runtime metadata support
 
What was learned in this process ?

=> How to add static metadata in traced functions for richer context and enhanced filtering/grouping in the LangSmith dashboard.

=> How to dynamically inject metadata at runtime within tracing to track additional execution details not known at design time.

