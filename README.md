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

Completed tracing pipeline and refined metadata usage
What was learned in the process ?

=> How to assemble a full traceable pipeline from retrieval through OpenAI completion and response generation, illustrating trace continuity.

=> The importance of clarity and correctness in metadata handling to maximize trace data quality and usability during debugging or evaluation.

Tweakings that were done for lesson 1 

1. Added setup and configuration for environment variables required for tracing and OpenAI API usage.

2. Introduced and applied the traceable decorator extensively to key functions to enable automated tracing of inputs, outputs, and errors.

3. Implemented a simple dummy retriever class to simulate vector database retrieval within the tracing pipeline, allowing tracing of retrieval steps without external dependencies.

4. Enhanced trace metadata use by introducing static metadata annotations on traced functions for richer context.

5. Enabled dynamic runtime metadata injection into traces for improved observability during execution.

6. Refined the flow and clarity of the tracing pipeline implementation, including better handling and documentation of metadata.

7. Corrected minor code details to ensure accurate trace capture and metadata propagation across the pipeline.

These changes improve the observability of the code execution through LangSmith’s tracing capabilities and demonstrate practical traceable pipeline setups.



