# Agricultural-RAG-Document-Retrieval
 

## Project Overview
Before an LLM can generate an answer, a retrieval system must identify the most relevant documents from a knowledge base.
This project focuses specifically on that retrieval stage. Given a smallholder farmer's question, the system ranks agricultural extension documents according to their relevance to the query.

The project evaluates and compares several retrieval approaches:
- BM25
- Dense retrieval
- Hybrid retrieval
- Cross-encoder reranking

The primary evaluation metric is **nDCG@5**, which measures how effectively the system ranks the most relevant documents within the top five results.

## Problem
An LLM's ability to generate a useful answer in a RAG system depends heavily on the quality of the information retrieved for it. Smallholder farmers often face difficulties accessing agricultural information because existing resources can be difficult, expensive, or time-consuming to search, while general search engines may return broad or irrelevant results. This project addresses this problem by developing a domain-specific retrieval engine that returns the top five most relevant agricultural extension documents for a farmer's question across key agronomic topics and twelve common crops in Africa.


## Dataset
This project consists of four datasets, each serving a different purpose.
1. documents.csv --- Contains the agricultural knowledge base that the retrieval model searches.
2. train_queries.csv --- Contains the training questions that simulate the types of questions a farmer may ask.
3. qrels_train.csv --- Contains the relevance judgments (also called qrels) used to evaluate how well a retrieval model ranks documents for each training query.
4.  test_queries.csv --- Contains the unseen farmer questions used to evaluate the retrieval system.

The knowledge base contains **695 agricultural extension factsheets** covering crop production, climate adaptation, pests, diseases, soil management, nutrient deficiencies, and fertilizer advice.

The dataset covers a range of crops relevant to agricultural production in Africa, including:

- Maize
- Tomato
- Rice
- Cassava
- Common beans
- Cowpea
- Groundnut
- Sorghum
- Plantain
- Yam
- Cocoa
- Pearl millet
- General crop-related topics

The agricultural materials are primarily focused on African contexts, with sources and examples spanning countries including **Nigeria, Ghana, Togo, Mali, Ethiopia, Kenya**, and other African countries.

This makes the retrieval task particularly relevant to agricultural information access in Sub-Saharan African farming contexts.

## Retrieval Approaches

## Experiments & Results

## Final Approach

## Competition Submission

## Technologies

## Project Structure

## Reproducibility

## Future Improvements
