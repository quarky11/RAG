# README: Retrieve-Augment-Generate (RAG) Framework

## Overview
Retrieve-Augment-Generate (RAG) is an advanced AI framework designed to blend information retrieval and language generation, enabling accurate, context-aware, and dynamic responses. It bridges the gap between raw data and conversational understanding, making it ideal for applications requiring both factual accuracy and human-like interaction.

---

## Key Components

### 1. **Retrieve**
- RAG retrieves relevant information from a knowledge base or external data sources (e.g., documents, databases, or APIs) based on user input.
- It ensures the responses are grounded in accurate and up-to-date information.

### 2. **Augment**
- Augmentation involves combining the retrieved data with user-provided input or context.
- This step ensures personalization and context alignment for each interaction.

### 3. **Generate**
- Using advanced language models, RAG generates coherent and contextually relevant responses.
- It maintains a conversational tone while adhering to factual accuracy.

---

![Flow_Diagram](https://github.com/user-attachments/assets/5a9d64f4-fdd3-4842-bb9a-52ba40b34574)

---

## Flow Diagram Explanation

### 1. **Pdf Reading**
- This process include about reading pdf document and make it into str data

### 2. **Convert to Chunks**
- this process include converting str data from step one in to list of str (chunks).

### 3. **Embedding and Storing**
- After we have chunks, we need to embedding it so it becomes a vectore and store it into vector database

### 4. **Llm Chaining**
- This is the process where user gave input and change it into embedding, doing the similarity search, and gave the best answer

### Application Video : https://drive.google.com/file/d/1umw_v1jGGhw_uIfD0igrfwzlu11V2lyU/view?usp=drive_link

### Resource : Alejandro AO - Software & Ai - Youtube 


