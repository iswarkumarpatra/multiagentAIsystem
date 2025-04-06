# 🛍️ AlgoMates: Multi-Agent AI-Powered E-commerce Recommendation System

## 🚀 Hackathon Submission: Hack the Future – A Gen AI Sprint Powered by Data

### 👥 Team AlgoMates
- **Iswar Kumar Patra** *(Team Leader)*
- **Saswat Kumar Pandey*

---

## 🧠 Problem Statement

Modern e-commerce platforms struggle to deliver personalized product recommendations due to manual, static, and non-adaptive systems. These outdated systems:
- Rely on rule-based segmentation
- Lack scalability and real-time adaptability
- Result in generic suggestions and reduced customer engagement

### 💡 Goal
To build a **multi-agent AI system** that provides **hyper-personalized recommendations** by dynamically learning from user behavior and product metadata in real-time.

---

## 🛠️ Our Solution: Multi-Agent Recommendation Architecture

Our architecture is composed of **three autonomous agents**, each specializing in a key aspect of personalization:

1. **Customer Agent**:
   - Tracks user behavior: browsing history, product clicks, purchase patterns, demographics
   - Builds dynamic user profiles updated in real-time
   - Stores data in a shared SQLite database

2. **Product Agent**:
   - Manages product metadata: tags, price, category, popularity
   - Generates embeddings using **Ollama-based on-prem LLMs**
   - Updates product vector space in SQLite for similarity matching

3. **Recommendation Agent**:
   - Central decision-maker that fetches user and product data
   - Utilizes **Gemma-2B model**, collaborative filtering, content-based filtering, and reinforcement learning
   - Delivers intelligent, personalized product recommendations

All agents **collaborate via a shared SQLite database**, enabling continuous learning and memory retention.

---

## ⚙️ Technologies Used

| Technology        | Purpose                                                |
|------------------|--------------------------------------------------------|
| **Ollama**        | On-prem LLMs for privacy-preserving, fast inference    |
| **Gemma-2B**      | Language understanding, agent communication, NLU tasks |
| **LangChain**     | Agent orchestration and prompt chaining                |
| **SQLite**        | Long-term memory store for user-agent interactions     |
| **Python**        | Backend, ML logic, API tooling                         |
| **Custom Tools**  | APIs, web scrapers, and ML models to enhance agents    |

---

## 🧾 Conclusion

We created a **scalable, modular, and intelligent** e-commerce recommendation system powered by **multi-agent collaboration and on-prem LLMs**. This architecture removes the need for manual tuning, learns in real-time, and adapts to user preferences—resulting in improved personalization, user engagement, and business ROI.

---

## 🔗 References

- [Ollama LLMs](https://ollama.com/)
- [Gemma-2B Model](https://ai.google.dev/gemma)
- [SQLite Documentation](https://sqlite.com)
- [LangChain Framework](https://www.langchain.com)

---

> Built with ❤️ by **AlgoMates** | AI for E-Commerce | Hack the Future 2025


