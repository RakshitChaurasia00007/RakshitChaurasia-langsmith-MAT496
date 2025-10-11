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




---

## What We Have Learned in Lesson 3

This lesson deep-dives into covering key concepts and practical implementations such as:

- Understanding multiple run types (LLM, Retriever, Tool, Chain, Prompt, Parser) and their use in LangSmith tracing.
- Setting up environment variables and tracing configurations correctly for seamless integration.
- Using the `@traceable` decorator, trace context manager, and `wrap_openai` wrapper for flexible and granular tracing control.
- Employing the RunTree API for manual, explicit trace creation enhancing observability.
- Best coding practices for metadata addition, error handling, timing, and tracing hierarchy.
- Integrating LangChain and LangGraph components with LangSmith tracing.
- Handling both standard and streaming LLM responses for comprehensive trace visibility.
- Using retriever runs and document metadata to improve trace render quality.
- Combining tools with LLMs in chains to enrich trace workflows.

---

## What Were Some of the Commits which were Done During the Lesson

- **Initial setup and environment variable configuration** enabling tracing with API keys and project context.
- **LLM run examples** showing how to format inputs and outputs, and include required metadata.
- **Streaming LLM runs** with reduce functions added for chunked output handling.
- **Retriever run examples** introducing formatted document retrieval with rich metadata support.
- **Tool call tracing improvements** incorporating function calls like weather fetching within the trace pipeline.
- **RunTree API implementation** giving fine control over manual tracing, run hierarchies, and metadata.
- **Wrap_openai wrapper usage** added to simplify trace logging in complex nested OpenAI calls.
- **Context manager tracing** usage demonstrated for block-level trace control.
- **Code polishing** with debug logs, error capturing, and enriched metadata injected in traces.

---

## What We Learned From These Commits

From the commits, we learned:

- The importance of precise environment setup and key configuration for automatic and manual tracing.
- How metadata and input/output message structure greatly influence trace clarity in LangSmith.
- The utility of streaming trace reducer functions for continuous outputs.
- How retriever runs enhance tracing visibility for document-based models.
- The effectiveness of combining LLMs and tools in a chained workflow for realistic applications.
- The flexibility and power of the RunTree API for explicit trace object management.
- Simplification of trace logging with the wrap_openai approach in complex systems.
- The added control and debugging benefits offered by the trace context manager.
- Best practices for maintaining trace consistency, dealing with errors, and timing.

---

## Tweaks and Modifications Done in the Updated Files

- Added granular metadata fields such as `version`, `component`, and application tags to enhance trace filtering and context.
- Split combined logic into finer-grained child runs like document formatting and model inference for better trace hierarchy.
- Incorporated debug print statements inside core functions to aid live troubleshooting.
- Wrapped OpenAI calls with try-except for robust error logging in traces.
- Added timing measurements on OpenAI API calls to track performance within traces.
- Parameterized models, temperature, and other inputs to increase flexibility and reuse.
- Switched to context manager tracing for explicit block-level control in suitable cases.
- Integrated usage of wrap_openai wrapper to reduce decorator boilerplate in nested calls.
- Strengthened environment variable setup documentation and added alternatives (inline, .env).
- Enhanced examples with LangGraph workflow visualizations showing data flow and integration.

---

# Conversational Threads Lesson

---

## What We Have Learned in the Lesson 4

This lesson introduces the concept of conversational threads in LangSmith tracing. We learned how to group related traces into threads, which represent conversations, by passing unique thread identifiers as metadata. Key takeaways include:

- Understanding threads as sequences of linked traces that form a conversation.
- Using metadata keys like `thread_id`, `session_id`, or `conversation_id` to associate traces.
- Generating unique UUIDs for thread identification.
- Implementing threaded tracing in practical retrieval-augmented generation (RAG) workflows.
- Running multiple queries with the same thread ID to maintain trace context and linkage.
- Observing trace grouping in LangSmith’s UI to improve analysis of conversation flow.

---

## What Were Some of the Commits Done During the Lesson

- Added UUID-based thread ID generation to uniquely identify conversations.
- Updated functions to accept and propagate thread metadata across traceable calls.
- Integrated `langsmith_extra` parameter to inject trace metadata when invoking functions.
- Enhanced examples by running multiple queries sharing the same thread_id.
- Added debugging statements to verify thread metadata propagation.
- Improved comments explaining thread-based grouping for better trace interpretation.

---

## What We Learned From These Commits



- The critical role of consistent thread metadata in effectively grouping conversational traces.
- How to use `langsmith_extra` metadata fields to explicitly link traces in the same conversation.
- Practical techniques for managing thread IDs through nested tracing calls.
- Benefits of debugging and logging thread association during development.
- The impact of thread grouping on trace visualization and conversational context understanding.

---

## Tweaks and Modifications

- Used Python's `uuid` module to generate clear and unique thread identifiers.
- Designed functions to optionally accept and merge metadata containing thread IDs.
- Added console logging to track thread ID usage and flow during execution.
- Consistently included `thread_id` in the `langsmith_extra` dictionary during API calls.
- Demonstrated multi-turn conversation examples sharing the same thread for realistic tracing.
- Added in-line comments emphasizing thread metadata importance and impact on trace grouping.
- Structured code for easier extension towards multi-session or multi-user conversational handling.

---

# Module 2 Lesson 1: Testing & Evaluation – Dataset Upload with LangSmith SDK

---

## What We Have Learned in the Lesson 1

In this lesson, we learned how to programmatically create and manage datasets in LangSmith using the SDK, supplementing the manual UI approaches. Key points include:

- Understanding the importance of structured datasets of input-output pairs for rigorous LLM testing.
- How to prepare example data derived from retrieval-augmented generation (RAG) or similar systems.
- Setting the necessary environment variables (`OPENAI_API_KEY`, `LANGSMITH_API_KEY`, `LANGSMITH_TRACING`, `LANGSMITH_PROJECT`) for authentication and tracing enablement.
- Loading environment variables from `.env` files versus inline setup.
- How to use the LangSmith Client to perform bulk upload of examples into a specific dataset via `client.create_examples`.
- The requirement for a valid dataset ID for successful uploads.
- Best practices for dataset construction reflecting real-world test cases.
- Importance of metadata for enhanced traceability and dataset management.

---

## What Were Some of the Commits Done During the Lesson

- Added environment setup with dotenv support and inline variable setting.
- Created example input-output pairs reflecting plausible RAG application queries and responses.
- Implemented batch creation of examples via the LangSmith SDK.
- Enhanced code with detailed inline comments and robust error handling.
- Polished metadata usage for both inputs and outputs.
- Added explicit dataset ID usage and validation in the upload process.
- Provided demonstration of using the dataset for downstream testing pipelines.

---
## What We Learned From These Commits

- SDK-based dataset creation greatly improves workflow automation and scalability.
- Adhering to data schema (question as input, output as response) ensures LangSmith compatibility.
- Managing API keys and environment settings correctly is essential for authentication in API calls.
- Bulk upload reduces manual overhead when dealing with large example sets.
- Proper dataset identification and management prevents upload errors and improves organization.
- Metadata enhances dataset documentation, enabling better trace filtering and analysis.
- Including relevant comments and logical structuring facilitates easier maintenance and onboarding.

---

## Tweaks and Modifications

- Added separation of environment var configurations and `.env` usage for flexibility.
- Incorporated richer example questions and customized answers deviating from samples to highlight originality.
- Improved metadata injection in example creation to boost trace and dataset interpretability.
- Structured input-output preparation for clarity and LangSmith compliance.
- Enhanced comments explaining dataset ID importance and upload prerequisites.
- Extended error handling to cover common authentication and data validity issues.
- Streamlined code to improve readability and ease of future updates.
- Demonstrated better practices with concrete code snippets for dataset upload workflows.

---

##  Module 3 Lesson 1 Begins 

## What have we learned in the Video of the LESSON 1 ?
- We have learned about the functionality of Langsmith playground.
- We can use the playground to check on the LLM prompts.
- We have also learned how we can run experiments on the datasets from the playground which can be very useful to test the single step of our application.

## Experiments & Comparisions of Different LLM's using DATASET
(More llike exploring the playground section of the LANGSMITH)
Below are the screenshots of how I have completly explored LANGSMITH PLAYGROUND .

Screenshot 1 the below screenshot shows us the dataset which was created in my langsmith playground due to modifications in the file 
<img width="1366" height="599" alt="image" src="https://github.com/user-attachments/assets/9306de1a-1e7f-4461-8a96-7c43c0204a32" />

Screenshot 2 When system is being asked to give output as a normal chatbot only 
<img width="1358" height="607" alt="image" src="https://github.com/user-attachments/assets/1c3918d5-d489-4685-ba5d-cd064fbe7518" />

Screenshot 3 when system is asked for being a professional lifestyle changer in 20's the response automatically changes .
<img width="1366" height="605" alt="image" src="https://github.com/user-attachments/assets/8367c012-fa6b-436f-bde4-1836271f480b" />

Below is screenshot for runnable sequence data 1
<img width="1366" height="646" alt="image" src="https://github.com/user-attachments/assets/bd2d2cfa-b6cc-4296-a156-a36bb08d1877" />
Screenshot of runnable sequence data 2
<img width="1366" height="647" alt="image" src="https://github.com/user-attachments/assets/477b731b-a08d-4a3a-a3ae-8508c7ab1334" />

Below we have the screenshot of the location from where we can change the service provider , model like which LLM model do you wanna use .
We can also change the temprature, Max Tokens , Frequency Penalty , Reasoning Effort where temprature is for controling the creativity , max output token is like the maximum length of the model's response, frequency penalty is like the process of reducing the words which are repeated in our response, reasonning effort is like how much a model is trying to think deeply .

<img width="1366" height="648" alt="image" src="https://github.com/user-attachments/assets/70f77205-71bd-47f7-8285-8f9d6b505ac9" />

Now there will be screenshot regarding comparision of output using different LLM models In one side we have O4-mini & O1-mini 
<img width="1366" height="606" alt="image" src="https://github.com/user-attachments/assets/961c05de-eb6b-413f-b6ba-271e80b93748" />
In the above screenshot we can see O4-MINI is more practical & energetic and O1-MINI is structured & thoughtful hence user can use the model according to their prefrences.

--
If we disable streaming we can run it with repititions.Repititions are usefule for consistency  and double check that we are able to respond towards a question correctly everytime.It is very useful when we have very high temprature. In the below screenshot by increasing repitition we have received 2 reponses for the same prompt.
<img width="1347" height="606" alt="image" src="https://github.com/user-attachments/assets/f2fc47fd-b4be-468c-bb55-f4a70e58254c" />

<img width="1366" height="650" alt="image" src="https://github.com/user-attachments/assets/a6554790-4610-4898-93ba-18679a77a5c7" />
The above screenshot show addition of schema in our process with description ,correctness strict & required string
<img width="1366" height="650" alt="image" src="https://github.com/user-attachments/assets/0328d9df-403f-4501-8094-c0cd5d165a53" />
Below is the return with 1 response using output schema and it must match with the function definition.

<img width="1363" height="609" alt="image" src="https://github.com/user-attachments/assets/8270d3c2-1402-43e3-b3de-6a91e72ff930" />

Now below I will attach the screenshot to show how Tabular view of our whole dataset looklike without running the LLM and after running the LLM on gpt O-4-MINI
First screenshot is about hoiw our dataset looks without running it on any LLM model .
<img width="1362" height="651" alt="image" src="https://github.com/user-attachments/assets/53b92808-aba0-4596-9139-9b7a66920128" />
Now our Second screenshot is about how the dataset will looklike when we will run it on GPT o-4-MINI having system prompt as "You are a chatbot "
<img width="1366" height="650" alt="image" src="https://github.com/user-attachments/assets/ff356a6a-7451-4eaf-8cda-1385c5742e03" />
## Now I will adjust the system prompt a bit by writinning 
Earlier our system prompt was just "You are a chatbot"  But now our system prompt is "You are a chatbot and you have to keep your answers short to 2-3 words that's all."
<img width="1366" height="645" alt="image" src="https://github.com/user-attachments/assets/09f59330-1893-4213-b138-70cdc9baca04" />

## Module 3 Lesson 2 Begins

## What we have learned in the Lessons of Video 2
   We learned how we can save our prompts in the prompt template. 
   These saved prompts include list of templated messages & optional model configuration and also optionally constructed output.
   We can pull these prompts directly in our code and also push these prompts up from our code into SDK.

## Hence Now we will Begin our Work According to lesson 2 Video 















