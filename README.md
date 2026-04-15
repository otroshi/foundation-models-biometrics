# Foundation Models and Biometrics

<a href="https://www.techrxiv.org/doi/full/10.36227/techrxiv.174119169.94570936" target="_blank">
  <img src="https://img.shields.io/badge/TechRxiv-002855.svg?logo=ieee" alt="TechRxiv">
</a>
<a href="https://forms.gle/NYNjhEKg6q4Pn1UM7" target="_blank">
  <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance">
</a>


## 🚀 About the Survey

This paper provides an overview of the recent advancements in foundation models and discusses potential applications of these models in the field of *biometrics*. **Foundation models**, such as **Large Language Models (LLMs)**, **Vision Language Models (VLMs)**, **Audio-Language Models (ALMs)**, and **Large Multi-modal Models (LMMs)**, are based on large neural networks which are trained with massive amounts of data and enable robust feature extraction for transfer learning. These models allow efficient zero-shot and few-shot learning, achieving state-of-the-art performance in downstream tasks.
Biometrics is also an active field of research, which involves various research problems, ranging from robust recognition to security and privacy in biometric systems. In this paper, we present an in-depth analysis of state-of-the-art methodologies regarding foundation multi-modal models, their advancements, and their applicability to biometrics tasks. We also highlight current limitations and provide insights into potential future research directions in the applications of foundation models in biometrics. To our knowledge, this paper is the **first survey** which investigates the *applications of foundation models in biometrics*.
[<a href="https://www.techrxiv.org/doi/full/10.36227/techrxiv.174119169.94570936" target="_blank">
  Link to pre-print
</a>]

The survey is structured as follows for clarity and readability:

- **Foundation Models**:
In this section, we review recent advancements in foundation models and mention state-of-the-art models. We catgeorise foundation models in four different catgories:
  - **Large Language Models (LLMs)**
  - **Vision Language Models (VLMs)**
  - **Audio-Language Models (ALMs)**
  - **Large Multi-modal Models (LMMs)**

- **Biometric Recognition and Security**:
In this section, we review the general pipeline of biometric systems. We describe attack points in biometric systems and discuss security and pprivacy threats.

- **Applications of Foundation Models in Biometrics**:
In this section, we review recent work on the applications of foundation models in biometrics:
  - **Foundation Models for Biometric Recognition**
  - **Foundation Models for Soft-biometric Detection**
  - **Foundation Models for Deepfake and Forgery Detection**
  - **Foundation Models for Anti-spoofing**
  - **Foundation Models for Synthetic Biometric Generation**



## 📚 Missing Papers

We will keep updating this survey and this git repository. Please contact the first author (hatef.otroshi@idiap.ch) or complete the following form to submit your paper for citation.  

👉 [Submit Your Paper](https://forms.gle/NYNjhEKg6q4Pn1UM7)

We appreciate your contributions and look forward to keeping this survey comprehensive and up to date!

## Foundation Models

### Large Language Models (LLMs)

<details>
| Model | Paper | Year | paper | code |
|---|---|---|---|---|
| GPT | Improving language understanding by generative pre-training | 2018 | [link](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | [link](https://github.com/openai/finetune-transformer-lm) |
| GPT-2 | Language models are unsupervised multitask learners | 2019 | [link](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | [link](https://github.com/openai/gpt-2) |
| GPT-3 | Language models are few-shot learners | 2020 | [link](https://proceedings.neurips.cc/paper_files/paper/2020/file/1457c0d6bfcb4967418bfb8ac142f64a-Paper.pdf) | [link](https://github.com/openai/gpt-3) |
| GPT-4 | GPT-4 technical report | 2023 | [link](https://arxiv.org/abs/2303.08774) | NA |
| o1 | OpenAI o1 System Card | 2024 | [link](https://arxiv.org/abs/2412.16720) | NA |
| o3-mini | OpenAI o3-mini System Card | 2025 | [link](https://cdn.openai.com/o3-mini-system-card-feb10.pdf) | NA |
| BERT | BERT: Pretraining of deep bidirectional transformers for language understanding | 2018 | [link](https://arxiv.org/abs/1810.04805) | [link](https://github.com/google-research/bert) |
| T5 | Exploring the limits of transfer learning with a unified text-to-text transformer | 2020 | [link](https://www.jmlr.org/papers/v21/20-074.html) | [link](https://github.com/google-research/text-to-text-transfer-transformer) |
| FLAN-T5 | Scaling instruction-finetuned language models | 2024 | [link](https://www.jmlr.org/papers/v25/23-0870.html) | [link](https://huggingface.co/docs/transformers/model_doc/flan-t5) |
| OPT | OPT: Open pre-trained transformer language models | 2020 | [link](https://arxiv.org/abs/2205.01068) | NA |
| Falcon | The Falcon Series of Open Language Models | 2023 | [link](https://arxiv.org/abs/2311.16867) | [link](https://huggingface.co/collections/tiiuae/falcon) |
| Mistral | Mistral 7B | 2023 | [link](https://arxiv.org/abs/2310.06825) | [link](https://github.com/mistralai/mistral-inference) |
| Mixtral | Mixtral of experts | 2023 | [link](https://arxiv.org/abs/2401.04088) | [link](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |
| LLaMA | LLaMA: Open and efficient foundation language models | 2023 | [link](https://arxiv.org/abs/2302.13971) | [link](https://github.com/meta-llama/llama) |
| LLaMA 2 | Llama 2: Open foundation and fine-tuned chat models | 2023 | [link](https://arxiv.org/abs/2307.09288) | [link](https://huggingface.co/collections/meta-llama/llama-2-family) |
| Vicuna | Judging LLM-as-a-judge with MT-bench and chatbot arena | 2023 | [link](https://proceedings.neurips.cc/paper_files/paper/2023/file/91f18a1287b398d378ef22505bf41832-Paper-Datasets_and_Benchmarks.pdf) | [link](https://github.com/lm-sys/FastChat/) |
| Gemma | Gemma: Open models based on Gemini research and technology | 2024 | [link](https://arxiv.org/abs/2403.08295) | [link](https://github.com/google-deepmind/gemma) |
| Gemma 2 | Gemma 2: Improving open language models at a practical size | 2024 | [link](https://arxiv.org/abs/2408.00118) | [link](https://github.com/google-deepmind/gemma) |
| Nemotron 4 | Nemotron-4 340B technical report | 2024 | [link](https://arxiv.org/abs/2406.11704) | [link](https://huggingface.co/nvidia/Nemotron-4-340B-Base) |
| Qwen | Qwen technical report | 2023 | [link](https://arxiv.org/abs/2309.16609) | [link](https://github.com/QwenLM/Qwen) |
| Qwen 2.5 | Qwen2.5 technical report | 2024 | [link](https://arxiv.org/abs/2412.15115) | [link](https://github.com/QwenLM/Qwen2.5) |
| Qwen 3 | Qwen3 technical report | 2025 | [link](https://arxiv.org/abs/2505.09388) | [link](https://github.com/QwenLM/qwen3) |
| Phi-4 | Phi-4 technical report | 2024 | [link](https://arxiv.org/abs/2412.08905) | [link](https://huggingface.co/microsoft/phi-4) |
| DeepSeek | DeepSeek LLM: Scaling open-source language models with longtermism | 2024 | [link](https://arxiv.org/abs/2401.02954) | [link](https://github.com/deepseek-ai/DeepSeek-LLM) |
| DeepSeek-V2 | DeepSeek-v2: A strong, economical, and efficient mixture-of-experts language model | 2024 | [link](https://arxiv.org/abs/2405.04434) | [link](https://github.com/deepseek-ai/DeepSeek-V2) |
| DeepSeek-V3 | DeepSeek-V3 technical report | 2024 | [link](https://arxiv.org/abs/2412.19437) | [link](https://github.com/deepseek-ai/DeepSeek-V3) |
| DeepSeek-R1 | DeepSeek-R1: Incentivizing reasoning capability in LLMs via reinforcement learnin | 2025 | [link](https://www.nature.com/articles/s41586-025-09422-z) | [link](https://github.com/deepseek-ai/DeepSeek-R1) |
| ReasonFlux | ReasonFlux: Hierarchical LLM reasoning via scaling thought templates | 2025 | [link](https://arxiv.org/abs/2502.06772) | [link](https://github.com/Gen-Verse/ReasonFlux) |

</details>

### Vision Language Models (VLMs)

<details>
TODO
</details>

### Audio-Language Models (ALMs)

<details>
TODO
</details>

### Large Multi-modal Models (LMMs)

<details>
TODO
</details>



## Applications of Foundation Models in Biometrics

### Foundation Models for Biometric Recognition

<details>
TODO
</details>

### Foundation Models for Soft-biometric Detection

<details>
TODO
</details>

### Foundation Models for Deepfake and Forgery Detection

<details>
TODO
</details>

### Foundation Models for Anti-spoofing

<details>
TODO
</details>

### Foundation Models for Synthetic Biometric Generation
<details>
TODO
</details>


## Citation

```bibtex
@article{fmbiometrics2025survey,
  title={Foundation Models and Biometrics: A Survey and Outlook},
  author={Hatef Otroshi Shahreza and S{\'e}bastien Marcel},
  journal={TechRxiv},
  doi={10.36227/techrxiv.174119169.94570936/v1},
  year={2025}
}
```