# Agricultural-RAG-Document-Retrieval
 

## Project Overview
The goal of this project is to build an agricultural document retrieval system that matches smallholder farmers' questions with relevant agricultural extension documents

The project evaluates and compares several retrieval approaches:
- BM25
- Dense retrieval
- Hybrid retrieval
- Cross-encoder reranking

The primary evaluation metric is **nDCG@5**, which measures how effectively the system ranks the most relevant documents within the top five results.

## Problem
An LLM's ability to generate a useful answer in a RAG system depends heavily on the quality of the information retrieved for it. Smallholder farmers often face difficulties accessing agricultural information because existing resources can be difficult, expensive, or time-consuming to search, while general search engines may return broad or irrelevant results. This project addresses this problem by developing a domain-specific retrieval engine that returns the top five most relevant agricultural extension documents for a farmer's question across key agronomic topics and twelve common crops in Africa.


## Dataset
This project uses four files, each serving a different purpose.
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

* Link to dataset: https://www.kaggle.com/competitions/agricultural-extension-rag-smart-retrieval-for-farmers/data

## Retrieval Approaches

Four retrieval approaches were implemented and evaluated:

1. BM25: BM25 was used as a lexical retrieval baseline, ranking documents based on the occurrence and importance of query terms.
 
2. Dense Retrieval: Dense retrieval was implemented using sentence-transformer embeddings and cosine similarity to capture semantic relationships between farmer questions and agricultural documents.

Several document representations were explored, including title-only, text-only, title + text, and a title-weighted representation. The final dense retrieval system used **`intfloat/e5-base-v2`** with the document representation: **'title + title + text`**

3. Hybrid Retrieval: BM25 and dense retrieval scores were combined using min-max normalization and a weighted hybrid scoring approach. Different BM25/dense weighting values were evaluated to determine whether combining lexical and semantic retrieval improved performance.

4. Cross-Encoder Reranking: Dense retrieval was first used to retrieve the top 50 candidate documents for each query. These candidates were then passed through a pretrained Cross-Encoder to produce more refined relevance scores and rerank the documents.


## Results

The four retrieval approaches were evaluated using **nDCG@5**, where higher scores indicate better ranking of relevant documents within the top five results.

| Retrieval Approach | nDCG@5 |
|---|---:|
| BM25 | 0.419 |
| Dense Retrieval | **0.791** |
| Hybrid Retrieval | 0.771 |
| Cross-Encoder Reranking | 0.720 |

Dense retrieval achieved the strongest performance among the approaches evaluated and was therefore selected as the final retrieval approach and used to generate the test-set predictions.


## Technologies  
- Python
- Pandas
- NumPy
- scikit-learn
- Sentence Transformers
- E5 (`intfloat/e5-base-v2`)
- Jupyter Notebook


## Project Structure
```text
Agricultural-RAG-Document-Retrieval/
├── README.md
└── agricultural_rag.ipynb
```
 
## Reproducibility

To reproduce the project:

1. Clone this repository.
2. Install the required Python dependencies:

   ```bash
   pip install -r requirements.txt

3. Obtain the competition dataset from Kaggle and place the required files in the appropriate location.
4. Open agricultural_rag.ipynb and run the notebook from top to bottom.


## Future Improvements
- **Query Expansion:** Experiment with agricultural synonyms, crop names, and domain-specific terminology to improve retrieval for differently phrased queries.
- **Retrieval Optimization:** Explore additional document representations and retrieval strategies to further improve ranking performance.
- **RAG Generation:** Extend the retrieval system into a complete RAG application by integrating an LLM that can use the retrieved agricultural documents to generate grounded responses.
