# RakshitChaurasia-langsmith-MAT496

This repository will include each and every detail of what I have learned and self-reflected throughout my journey of learning LangSmith from basic.

---

## Lesson 1

### Learning Summary from the Video of Lesson 1  
Learned to use LangSmith Python SDK for tracing, including setting environment variables, applying the traceable decorator to functions, and utilizing metadata annotation to enrich trace data. The updated file introduces a dummy retriever example for simulating vector DB retrieval and demonstrates runtime metadata usage.

---

### Set up environment variables for LangSmith and OpenAI  
**What was learned in this process?**

- How to correctly configure environment variables required to enable LangSmith tracing and OpenAI API access.  
- Importance of setting `LANGSMITH_TRACING` and project keys for the LangSmith SDK to function.

---

### Implemented function tracing with traceable decorator  
**What was learned in this process?**

- How to use the `traceable` decorator from LangSmith SDK to log function calls, capture inputs, outputs, and errors automatically.  
- How the decorator creates a trace run tree supporting asynchronous background logging without blocking main execution.

---

### Added and used a dummy vector database retriever for tracing demos  
**What was learned in this process?**

- How to simulate a vector DB retriever for Retrieval-Augmented Generation (RAG) pipelines using a simple dummy class for testing.  
- How such a retriever integrates within tracing to demonstrate end-to-end observability of data retrieval steps.

---

### Incorporated metadata annotations and runtime metadata support  
**What was learned in this process?**

- How to add static metadata in traced functions for richer context and enhanced filtering/grouping in the LangSmith dashboard.  
- How to dynamically inject metadata at runtime within tracing to track additional execution details not known at design time.

---

### Completed tracing pipeline and refined metadata usage  
**What was learned in this process?**

- How to assemble a full traceable pipeline from retrieval through OpenAI completion and response generation, illustrating trace continuity.  
- The importance of clarity and correctness in metadata handling to maximize trace data quality and usability during debugging or evaluation.

---

### Tweakings that were done for Lesson 1

1. Added setup and configuration for environment variables required for tracing and OpenAI API usage.  
2. Introduced and applied the `traceable` decorator extensively to key functions to enable automated tracing of inputs, outputs, and errors.  
3. Implemented a simple dummy retriever class to simulate vector database retrieval within the tracing pipeline, allowing tracing of retrieval steps without external dependencies.
4. Enhanced trace metadata use by introducing static metadata annotations on traced functions for richer context.  
5. Enabled dynamic runtime metadata injection into traces for improved observability during execution.  
6. Refined the flow and clarity of the tracing pipeline implementation, including better handling and documentation of metadata.  
7. Corrected minor code details to ensure accurate trace capture and metadata propagation across the pipeline.

These changes improve the observability of the code execution through LangSmith’s tracing capabilities and demonstrate practical traceable pipeline setups.
# Lesson 2 - Types of Runs and LangSmith Tracing

## Types of Runs Supported by LangSmith

- **LLM**: Invokes large language models; supports both standard and streaming modes.
- **Retriever**: Retrieves documents from sources like databases, indexers. Supports tracing of document retrieval steps.
- **Tool**: Executes function calls, allowing for custom actions during a run.
- **Chain**: Combines multiple runs (LLM, Retriever, Tool) into a larger pipeline for complex workflows.
- **Prompt**: Hydrates prompts with structured context for LLMs.
- **Parser**: Extracts structured data from responses and response chunks.

## Setup and Environment Configuration

- How to correctly set API keys for OpenAI and LangSmith as environment variables (`OPENAI_API_KEY`, `LANGSMITH_API_KEY`) or via `.env` files using `dotenv`.
- How to enable tracing globally with `LANGSMITH_TRACING="true"` and specify project name.

## Usage of Tracing for Different Runs

- **LLM**: How to trace chat-based models, with an example showing the input and output formats, including optional metadata (`ls_provider`, `ls_model_name`).
- **Streaming LLM**: How to handle chunked responses with a `reduce_fn()` to assemble the final output; demonstrated with an example.
- **Retriever**: How to trace document retrieval, return proper document objects (`page_content`, `type`, `metadata`) for proper visualization in traces.
- **Tool Calls**: How to trace custom function calls, like fetching weather data, and how to correctly include API keys.

## Additional Learnings

- Emphasis on how to format messages and responses for LangSmith tracing.
- How to specify run types via decorator `@traceable(run_type="...")`.
- How to inject metadata at the function or call level to improve trace clarity.

## Summary

Lesson 2 elaborates on practical implementation with multiple run types, illustrating the design choices and setup steps needed for comprehensive tracing coverage across different components of an LLM-powered application, emphasizing the importance of correct API key setup, metadata usage, and handling both streaming and non-streaming processes.

---

## Commit Messages for Lesson 2

- **feat: initial setup and environment configuration for tracing**  
  Learned how to configure API keys, enable LangSmith tracing, and specify project context using environment variables and dotenv files.

- **feat: added LLM run example with proper message formatting and metadata**  
  Explored how to trace chat LLM runs with examples showing structured input/output formats and metadata fields such as model name and provider.

- **feat: implemented streaming LLM run with reduce function**  
  Learned to handle streaming LLM responses, reduce partial chunks into final output, and trace streaming interactions effectively.

- **feat: added retriever run example with document format and metadata**  
  Added tracing for document retrieval using retriever runs, demonstrated how to return documents with text content and metadata for better trace visualization.

- **feat: incorporated tool call tracing with weather example**  
  Extended tool call tracing with a practical weather-fetching example, combined it with LLM calls, enhanced examples with environment variable setup.

---

## Tweak Summary for Lesson 2

- Added extensive run type examples covering LLM, streaming LLM, Retriever, and Tool types for comprehensive tracing.
- Improved documentation and comments explaining required input/output formats for each run type.
- Included sample metadata fields such as `ls_provider` and `ls_model_name` for richer trace context.
- Enhanced environment setup instructions for API keys and tracing enablement.
- Added reduce function example to showcase handling of streaming data in traces.
- Refined document retrieval example with detailed document metadata for better UI rendering in LangSmith.

---

## Original File Note

The original file remains unchanged as the base reference for Lesson 2 content.
