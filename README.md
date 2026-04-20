# Foundation Models and Biometrics: A Survey and Outlook

<div align="center">

  <a href="https://otroshi.github.io/foundation-models-biometrics" target="_blank">
    <img src="https://img.shields.io/badge/website-live-orange" alt="Website">
  </a>
  <a href="https://ieeexplore.ieee.org/abstract/document/11137396" target="_blank">
    <img src="https://img.shields.io/badge/IEEE-TIFS-00629B?logo=ieee" alt="IEEE-TIFS">
  </a>
  <a href="https://www.techrxiv.org/doi/full/10.36227/techrxiv.174119169.94570936" target="_blank">
    <img src="https://img.shields.io/badge/TechRxiv-002855.svg?logo=ieee" alt="TechRxiv">
  </a>
  <a href="https://forms.gle/NYNjhEKg6q4Pn1UM7" target="_blank">
    <img src="https://img.shields.io/badge/Maintained%3F-yes-green.svg" alt="Maintenance">
  </a>

</div>


## 🚀 About the Survey

This paper provides an overview of the recent advancements in foundation models and discusses potential applications of these models in the field of *biometrics*. **Foundation models**, such as **Large Language Models (LLMs)**, **Vision Language Models (VLMs)**, **Audio-Language Models (ALMs)**, and **Large Multi-modal Models (LMMs)**, are based on large neural networks which are trained with massive amounts of data and enable robust feature extraction for transfer learning. These models allow efficient zero-shot and few-shot learning, achieving state-of-the-art performance in downstream tasks.
Biometrics is also an active field of research, which involves various research problems, ranging from robust recognition to security and privacy in biometric systems. In this paper, we present an in-depth analysis of state-of-the-art methodologies regarding foundation multi-modal models, their advancements, and their applicability to biometrics tasks. We also highlight current limitations and provide insights into potential future research directions in the applications of foundation models in biometrics. To our knowledge, this paper is the **first survey** which investigates the *applications of foundation models in biometrics*.
[<a href="https://www.techrxiv.org/doi/full/10.36227/techrxiv.174119169.94570936" target="_blank">
  Link to pre-print
</a>] [<a href="https://ieeexplore.ieee.org/abstract/document/11137396" target="_blank">
  Link to paper on IEEE-Xplore (Open Access)
</a>]

The survey is structured as follows for clarity and readability:

- [**Foundation Models**](#-foundation-models):
In this section, we review recent advancements in foundation models and mention state-of-the-art models. We catgeorise foundation models in four different catgories:
  - **Large Language Models (LLMs)**
  - **Vision Language Models (VLMs)**
  - **Audio-Language Models (ALMs)**
  - **Large Multi-modal Models (LMMs)**

- **Biometric Recognition and Security**:
In this section, we review the general pipeline of biometric systems. We describe attack points in biometric systems and discuss security and privacy threats. For information about this section, we refer the readers to Section III of our survey paper.

- [**Applications of Foundation Models in Biometrics**](#-applications-of-foundation-models-in-biometrics):
In this section, we review recent papers on the applications of foundation models in biometrics:
  - **Foundation Models for Biometric Recognition**
  - **Foundation Models for Soft-biometric Detection**
  - **Foundation Models for Deepfake and Forgery Detection**
  - **Foundation Models for Anti-spoofing**
  - **Foundation Models for Synthetic Biometric Generation**



## ✨ Foundation Models

In this section, we review recent advancements in foundation models and mention state-of-the-art models. We catgeorise foundation models in four different catgories:

- [Large Language Models (LLMs)](#large-language-models-llms)
- [Vision Language Models (VLMs)](#vision-language-models-vlms)
- [Audio-Language Models (ALMs)](#audio-language-models-ams)
- [Large Multi-modal Models (LMMs)](#large-multi-modal-models-lmms)

### Large Language Models (LLMs)


| Model | Paper Title | Year | Paper | Code |
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


### Vision Language Models (VLMs)


| Model | Paper Title | Year | Paper | Code |
|---|---|---|---|---|
| DINO | Emerging properties in self-supervised vision transformers | 2021 | [link](https://openaccess.thecvf.com/content/ICCV2021/papers/Caron_Emerging_Properties_in_Self-Supervised_Vision_Transformers_ICCV_2021_paper.pdf) | [link](https://github.com/facebookresearch/dino) |
| DINOv2 | Dinov2: Learning robust visual features without supervision | 2023 | [link](https://openreview.net/pdf?id=a68SUt6zFt) | [link](https://github.com/facebookresearch/dinov2) |
| BEiT | Beit: Bert pre-training of image transformers | 2021 | [link](https://openreview.net/pdf?id=p-BhZSz59o4) | [link](https://github.com/microsoft/unilm) |
| CLIP | Learning transferable visual models from natural language supervision | 2021 | [link](https://proceedings.mlr.press/v139/radford21a) | [link](https://github.com/openai/CLIP) |
| ALIGN | Scaling up visual and vision-language representation learning with noisy text supervision | 2021 | [link](https://proceedings.mlr.press/v139/jia21b.html) | NA |
| FLAVA | Flava: A foundational language and vision alignment model | 2022 | [link](https://openaccess.thecvf.com/content/CVPR2022/html/Singh_FLAVA_A_Foundational_Language_and_Vision_Alignment_Model_CVPR_2022_paper) | [link](https://flava-model.github.io/) |
| Florence | Florence: A new foundation model for computer vision | 2021 | [link](https://arxiv.org/abs/2111.11432) | NA |
| OFA | Ofa: Unifying architectures, tasks, and modalities through a simple sequence-to-sequence learning framework | 2022 | [link](http://proceedings.mlr.press/v162/wang22al.html) | [link](https://github.com/ofa-sys/ofa) |
| Unified-IO | Unified-io: A unified model for vision, language, and multi-modal tasks | 2022 | [link](https://openreview.net/pdf?id=E01k9048soZ) | [link](https://unified-io.allenai.org/) |
| AIM | Scalable Pre-training of Large Autoregressive Image Models | 2024 | [link](https://proceedings.mlr.press/v235/el-nouby24a.html) | [link](https://github.com/apple/ml-aim) |
| AIMv2 | Multimodal Autoregressive Pre-training of Large Vision Encoders | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Fini_Multimodal_Autoregressive_Pre-training_of_Large_Vision_Encoders_CVPR_2025_paper.html) | [link](https://github.com/apple/ml-aim) |
| BLIP | Blip: Bootstrapping language-image pre-training for unified vision-language understanding and generation | 2022 | [link](https://proceedings.mlr.press/v162/li22n.html) | [link](https://github.com/salesforce/BLIP) |
| BLIP 2 | Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models | 2023 | [link](https://proceedings.mlr.press/v202/li23q) | [link](https://github.com/salesforce/LAVIS/tree/main/projects/blip2) |
| SigLIP | Sigmoid loss for language image pre-training | 2023 | [link](https://openaccess.thecvf.com/content/ICCV2023/html/Zhai_Sigmoid_Loss_for_Language_Image_Pre-Training_ICCV_2023_paper.html) | [link](https://github.com/google-research/big_vision?tab=readme-ov-file#image-text-training-with-siglip) |
| SigLIP 2 | Siglip 2: Multilingual vision-language encoders with improved semantic understanding, localization, and dense features | 2025 | [link](https://arxiv.org/abs/2502.14786) | [link](https://github.com/google-research/big_vision/blob/main/big_vision/configs/proj/image_text/README_siglip2.md) |
| OpenCLIP | Reproducible Scaling Laws for Contrastive Language-Image Learning | 2023 | [link](https://openaccess.thecvf.com/content/CVPR2023/html/Cherti_Reproducible_Scaling_Laws_for_Contrastive_Language-Image_Learning_CVPR_2023_paper) | [link](https://github.com/laion-ai/scaling-laws-openclip) |
| SAM | Segment anything | 2023 | [link](https://openaccess.thecvf.com/content/ICCV2023/html/Kirillov_Segment_Anything_ICCV_2023_paper.html) | [link](https://github.com/facebookresearch/segment-anything) |
| SAM~2 | Sam 2: Segment anything in images and videos | 2024 | [link](https://openreview.net/pdf?id=Ha6RTeWMd0) | [link](https://github.com/facebookresearch/sam2) |
| DALL-E | Zero-shot text-to-image generation | 2021 | [link](https://proceedings.mlr.press/v139/ramesh21a.html) | NA |
| DALL-E 2 | Hierarchical text-conditional image generation with clip latents | 2022 | [link](https://arxiv.org/abs/2204.06125) | NA |
| DALL-E~3 | Improving image generation with better captions | 2023 | [link](https://arxiv.org/abs/2006.11807) | NA |
| Stable Diffusion | High-resolution image synthesis with latent diffusion models | 2022 | [link](https://openaccess.thecvf.com/content/CVPR2022/html/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.html?utm_source=rns.dwaiai.de) | [link](https://github.com/CompVis/latent-diffusion) |
| Imagen 3 | Imagen 3 | 2024 | [link](https://arxiv.org/abs/2408.07009) | NA |
| Edify | Edify Image: High-Quality Image Generation with Pixel Space Laplacian Diffusion Models | 2024 | [link](https://arxiv.org/abs/2411.07126) | NA |
| LlamaGen | Autoregressive Model Beats Diffusion: Llama for Scalable Image Generation | 2024 | [link](https://arxiv.org/abs/2406.06525) | [link](https://github.com/FoundationVision/LlamaGen) |
| GPT-4V | GPT-4V | 2024 | [link](https://cdn.openai.com/papers/GPTV_System_Card.pdf) | NA |
| MiniGPT-4 | Minigpt-4: Enhancing vision-language understanding with advanced large language models | 2023 | [link](https://openreview.net/pdf?id=1tZbq88f27) | [link](https://minigpt-4.github.io/) |
| Flamingo | Flamingo: a Visual Language Model for Few-Shot Learning | 2022 | [link](https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html) | NA |
| LLaVa | Improved baselines with visual instruction tuning | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_Improved_Baselines_with_Visual_Instruction_Tuning_CVPR_2024_paper.html) | [link](https://llava-vl.github.io/) |
| Video-LLaVa | Video-LLaVA: Learning United Visual Representation by Alignment Before Projection | 2023 | [link](https://aclanthology.org/2024.emnlp-main.342/) | [link](https://github.com/PKU-YuanGroup/Video-LLaVA) |
| Pixtral | Pixtral 12B | 2024 | [link](https://arxiv.org/abs/2410.07073) | [link](https://huggingface.co/mistralai/Pixtral-12B-2409) |
| Phi-3.5-Vision | Phi-3 technical report: A highly capable language model locally on your phone | 2024 | [link](https://arxiv.org/abs/2404.14219) | [link](https://huggingface.co/microsoft/Phi-3.5-vision-instruct) |
| VILA | Vila: On pre-training for visual language models | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Lin_VILA_On_Pre-training_for_Visual_Language_Models_CVPR_2024_paper.html) | [link](https://github.com/NVlabs/VILA) |
| NVILA | NVILA: Efficient frontier visual language models | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_NVILA_Efficient_Frontier_Visual_Language_Models_CVPR_2025_paper.html) | [link](https://github.com/NVlabs/VILA) |
| VILA-U | Vila-u: a unified foundation model integrating visual understanding and generation | 2024 | [link](https://openreview.net/pdf?id=02haSpO453) | [link](https://github.com/mit-han-lab/vila-u) |
| TokenFlow | Tokenflow: Unified image tokenizer for multimodal understanding and generation | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Qu_TokenFlow_Unified_Image_Tokenizer_for_Multimodal_Understanding_and_Generation_CVPR_2025_paper.html) | [link](https://github.com/ByteVisionLab/TokenFlow) |
| VAR | Visual Autoregressive Modeling: Scalable Image Generation via Next-Scale Prediction | 2024 | [link](https://proceedings.neurips.cc/paper_files/paper/2024/hash/9a24e284b187f662681440ba15c416fb-Abstract-Conference.html) | [link](https://github.com/FoundationVision/VAR) |
| InstructBLIP | Instructblip: Towards general-purpose vision-language models with instruction tuning | 2023 | [link](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a6a435e75419a836fe47ab6793623e6-Abstract-Conference.html) | [link](https://github.com/salesforce/LAVIS/tree/main/projects/instructblip) |
| Yi-VL | Yi: Open foundation models by 01. ai | 2024 | [link](https://arxiv.org/abs/2403.04652) | [link](https://huggingface.co/01-ai/Yi-VL-6B) |
| Qwen-VL | Qwen-vl: A versatile vision-language model for understanding, localization, text reading, and beyond | 2023 | [link](https://arxiv.org/abs/2308.12966) | [link](https://github.com/QwenLM/Qwen-VL) |
| Qwen2-VL | Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution | 2024 | [link](https://arxiv.org/abs/2409.12191) | [link](https://huggingface.co/collections/Qwen/qwen2-vl) |
| Qwen2.5-VL | Qwen2.5-VL Technical Report | 2025 | [link](https://arxiv.org/abs/2502.13923) | [link](https://huggingface.co/collections/Qwen/qwen25-vl) |
| InternVL | Internvl: Scaling up vision foundation models and aligning for generic visual-linguistic tasks | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Chen_InternVL_Scaling_up_Vision_Foundation_Models_and_Aligning_for_Generic_CVPR_2024_paper.html) | [link](http://github.com/opengvlab/internvl) |
| InternVL 1.5 | How far are we to gpt-4v? closing the gap to commercial multimodal models with open-source suites | 2024 | [link](https://arxiv.org/abs/2404.16821) | [link](http://github.com/opengvlab/internvl) |
| InternVL3 | Internvl3: Exploring advanced training and test-time recipes for open-source multimodal models | 2025 | [link](https://arxiv.org/abs/2504.10479) | [link](http://github.com/opengvlab/internvl) |
| InternVideo2 | InternVideo2: Scaling Foundation Models for Multimodal Video Understanding | 2024 | [link](https://arxiv.org/abs/2403.15377) | [link](https://github.com/opengvlab/internvideo) |
| LLaVa-OneVision | LLaVA-OneVision: Easy Visual Task Transfer | 2024 | [link](https://openreview.net/pdf?id=zKv8qULV6n) | [link](https://llava-vl.github.io/blog/2024-08-05-llava-onevision/) |
| LLaVa-NeXT | Llava-next-interleave: Tackling multi-image, video, and 3d in large multimodal models | 2024 | [link](https://arxiv.org/abs/2407.07895) | [link](https://github.com/LLaVA-VL/LLaVA-NeXT) |
| CogVLM2 | Cogvlm2: Visual language models for image and video understanding | 2024 | [link](https://arxiv.org/abs/2408.16500) | [link](https://github.com/zai-org/CogVLM2) |
| Bunny | Efficient multimodal learning from data-centric perspective | 2024 | [link](https://arxiv.org/abs/2402.11530) | [link](https://github.com/BAAI-DCAI/Bunny) |
| Chameleon | Chameleon: Mixed-Modal Early-Fusion Foundation Models | 2024 | [link](https://arxiv.org/abs/2405.09818) | [link](https://github.com/facebookresearch/chameleon) |
| Apollo | Apollo: An Exploration of Video Understanding in Large Multimodal Models | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Zohar_Apollo__An_Exploration_of_Video_Understanding_in_Large_Multimodal_CVPR_2025_paper.html) | [link](https://apollo-lmms.github.io/) |
| DeepSeek-VL | DeepSeek-VL: Towards Real-World Vision-Language Understanding | 2024 | [link](https://arxiv.org/abs/2403.05525) | [link](https://github.com/deepseek-ai/DeepSeek-VL) |
| DeepSeek-VL2 | DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding | 2024 | [link](https://arxiv.org/abs/2412.10302) | [link](https://github.com/deepseek-ai/DeepSeek-VL2) |
| Emu 3 | Emu3: Next-Token Prediction is All You Need | 2024 | [link](https://arxiv.org/abs/2409.18869) | [link](https://github.com/baaivision/Emu3) |
| Janus | Janus: Decoupling visual encoding for unified multimodal understanding and generation | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_Janus_Decoupling_Visual_Encoding_for_Unified_Multimodal_Understanding_and_Generation_CVPR_2025_paper.html) | [link](https://github.com/deepseek-ai/Janus) |
| JanusFlow | JanusFlow: Harmonizing Autoregression and Rectified Flow for Unified Multimodal Understanding and Generation | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Ma_JanusFlow_Harmonizing_Autoregression_and_Rectified_Flow_for_Unified_Multimodal_Understanding_CVPR_2025_paper.html) | [link](https://github.com/deepseek-ai/Janus) |
| Janus-Pro | Janus-Pro: Unified Multimodal Understanding and Generation with Data and Model Scaling | 2025 | [link](https://arxiv.org/abs/2501.17811) | [link](https://github.com/deepseek-ai/Janus) |
| Movie Gen | Movie Gen: A Cast of Media Foundation Models | 2024 | [link](https://arxiv.org/abs/2410.13720) | NA |
| Mochi | [blog] Mochi 1: A new SOTA in open text-to-video | 2024 | [link](https://www.genmo.ai/blog) | [link](https://github.com/genmoai/mochi) |
| Imagen Video | Imagen video: High definition video generation with diffusion models | 2022 | [link](https://arxiv.org/abs/2210.02303) | NA |
| Make-A-Video | Make-A-Video: Text-to-Video Generation without Text-Video Data | 2023 | [link](https://openreview.net/pdf?id=nJfylDvgzlq) | [link](https://make-a-video.github.io/) |
| Tune-A-Video | Tune-a-video: One-shot tuning of image diffusion models for text-to-video generation | 2023 | [link](http://openaccess.thecvf.com/content/ICCV2023/html/Wu_Tune-A-Video_One-Shot_Tuning_of_Image_Diffusion_Models_for_Text-to-Video_Generation_ICCV_2023_paper.html) | [link](https://tuneavideo.github.io/) |
| PixelDance | Make pixels dance: High-dynamic video generation | 2024 | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Zeng_Make_Pixels_Dance_High-Dynamic_Video_Generation_CVPR_2024_paper.html) | [link](https://makepixelsdance.github.io/) |
| CogVideoX | CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer | 2024 | [link](https://openreview.net/pdf?id=LQzN6TRFg9) | [link](https://github.com/zai-org/CogVideo) |
| FlashVideo | FlashVideo:Flowing Fidelity to Detail for Efficient High-Resolution Video Generation | 2025 | [link](https://ojs.aaai.org/index.php/AAAI/article/view/38270) | [link](https://github.com/FoundationVision/FlashVideo) |
| Goku | Goku: Flow Based Video Generative Foundation Models | 2025 | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_Goku_Flow_Based_Video_Generative_Foundation_Models_CVPR_2025_paper.html) | [link](https://github.com/Saiyan-World/goku) |
| T2V | Step-Video-T2V Technical Report: The Practice, Challenges, and Future of Video Foundation Model | 2025 | [link](https://arxiv.org/abs/2502.10248) | [link](https://github.com/stepfun-ai/Step-Video-T2V) |
| Sora | [blog] Sora: Creating Video from Text | 2024 | [link](https://openai.com/index/sora/) | NA |


### Audio-Language Models (ALMs)


| Model | Paper Title | Year | Paper | Code |
|---|---|---|---|---|
| Wav2Vec 2.0 | wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations | 2020 | [link](https://proceedings.neurips.cc/paper/2020/hash/92d1e1eb1cd6f9fba3227870bb6d7f07-Abstract.html) | [link](https://github.com/facebookresearch/fairseq) |
| HuBERT | Hubert: Self-supervised speech representation learning by masked prediction of hidden units | 2021 | [link](https://arxiv.org/abs/2106.07447) | [link](https://github.com/facebookresearch/fairseq/tree/main/examples/hubert) |
| WavLM | Wavlm: Large-scale self-supervised pre-training for full stack speech processing | 2022 | [link](https://arxiv.org/abs/2110.13900) | [link](https://github.com/microsoft/UniSpeech) |
| Whisper | Robust speech recognition via large-scale weak supervision | 2023 | [link](https://proceedings.mlr.press/v202/radford23a.html) | [link](https://github.com/openai/whisper) |
| USM | Google usm: Scaling automatic speech recognition beyond 100 languages | 2023 | [link](https://arxiv.org/abs/2303.01037) | NA |
| UniAudio | Uniaudio: An audio foundation model toward universal audio generation | 2023 | [link](https://arxiv.org/abs/2310.00704) | [link](https://github.com/yangdongchao/UniAudio) |
| MERT | Mert: Acoustic music understanding model with large-scale self-supervised training | 2023 | [link](https://openreview.net/pdf?id=w3YZ9MSlBu) | [link](https://github.com/yizhilll/MERT) |
| CLAP | Clap learning audio concepts from natural language supervision | 2023 | [link](https://arxiv.org/abs/2206.04769) | [link](https://github.com/microsoft/CLAP) |
| SenseVoice | Funaudiollm: Voice understanding and generation foundation models for natural interaction between humans and llms | 2024 | [link](https://arxiv.org/abs/2407.04051) | [link](https://github.com/FunAudioLLM/SenseVoice) |
| CosyVoice | Cosyvoice: A scalable multilingual zero-shot text-to-speech synthesizer based on supervised semantic tokens | 2024 | [link](https://arxiv.org/abs/2407.05407) | [link](https://github.com/FunAudioLLM/CosyVoice) |
| Vall-E | Neural codec language models are zero-shot text to speech synthesizers | 2023 | [link](https://arxiv.org/abs/2301.02111) | NA |
| SpeechT5 | Speecht5: Unified-modal encoder-decoder pre-training for spoken language processing | 2021 | [link](https://aclanthology.org/2022.acl-long.393/) | [link](https://github.com/microsoft/speecht5) |
| SLM | Slm: Bridge the thin gap between speech and text foundation models | 2023 | [link](https://arxiv.org/abs/2310.00230) | NA |
| AudioGPT | Audiogpt: Understanding and generating speech, music, sound, and talking head | 2024 | [link](https://ojs.aaai.org/index.php/AAAI/article/view/30570) | [link](https://github.com/AIGC-Audio/AudioGPT) |
| SpeechGPT | SpeechGPT: Empowering Large Language Models with Intrinsic Cross-Modal Conversational Abilities | 2023 | [link](https://aclanthology.org/2023.findings-emnlp.1055/) | [link](https://github.com/0nutation/SpeechGPT) |
| AudioPaLM | Audiopalm: A large language model that can speak and listen | 2023 | [link](https://arxiv.org/abs/2306.12925) | NA |
| SALMONN | SALMONN: Towards Generic Hearing Abilities for Large Language Models | 2024 | [link](https://openreview.net/pdf?id=14rn7HpKVk) | [link](https://github.com/bytedance/SALMONN) |
| WavLLM | Wavllm: Towards robust and adaptive speech large language model | 2024 | [link](https://aclanthology.org/2024.findings-emnlp.263/) | [link](https://github.com/microsoft/SpeechT5/tree/main/WavLLM) |
| Pengi | Pengi: An audio language model for audio tasks | 2023 | [link](https://proceedings.neurips.cc/paper_files/paper/2023/hash/3a2e5889b4bbef997ddb13b55d5acf77-Abstract-Conference.html) | [link](https://github.com/microsoft/Pengi) |
| LTU | Listen, Think, and Understand | 2024 | [link](https://openreview.net/pdf?id=nBZBPXdJlC) | [link](https://github.com/YuanGongND/ltu) |
| GAMA | GAMA: A Large Audio-Language Model with Advanced Audio Understanding and Complex Reasoning Abilities | 2024 | [link](https://aclanthology.org/2024.emnlp-main.361/) | [link](https://sreyan88.github.io/gamaaudio/) |
| Qwen2-Audio | Qwen2-audio technical report | 2024 | [link](https://arxiv.org/abs/2407.10759) | [link](https://github.com/qwenlm/qwen2-audio) |
| SeamlessM4T | SeamlessM4T-Massively Multilingual \& Multimodal Machine Translation | 2023 | [link](https://arxiv.org/abs/2308.11596) | [link](https://github.com/facebookresearch/seamless_communication) |
| Step-Audio | Step-Audio: Unified Understanding and Generation in Intelligent Speech Interaction | 2025 | [link](https://arxiv.org/abs/2502.11946) | [link](https://github.com/stepfun-ai/Step-Audio) |
| MusicLM | Musiclm: Generating music from text | 2023 | [link](https://arxiv.org/abs/2301.11325) | NA |
| AudioLDM | Audioldm: Text-to-audio generation with latent diffusion models | 2023 | [link](https://arxiv.org/abs/2301.12503) | [link](https://audioldm.github.io/) |


### Large Multi-modal Models (LMMs)

| Model | Paper Title | Year | Paper | Code |
|---|---|---|---|---|
| AudioCLIP | Audioclip: Extending clip to image, text and audio | 2022 | [link](https://arxiv.org/abs/2106.13043) | [link](https://github.com/AndreyGuzhov/AudioCLIP) |
| 4M | 4m: Massively multimodal masked modeling | 2023 | [link](https://proceedings.neurips.cc/paper_files/paper/2023/hash/b6446566965fa38e183650728ab70318-Abstract-Conference.html) | [link](https://4m.epfl.ch/) |
| ImageBind | Imagebind: One embedding space to bind them all | 2023 | [link](https://openaccess.thecvf.com/content/CVPR2023/html/Girdhar_ImageBind_One_Embedding_Space_To_Bind_Them_All_CVPR_2023_paper.html) | [link](https://github.com/facebookresearch/imagebind) |
| PandaGPT | Pandagpt: One model to instruction-follow them all | 2023 | [link](https://aclanthology.org/2023.tllm-1.2/) | [link](https://panda-gpt.github.io/) |
| NeXT-GPT | NExT-GPT: Any-to-Any Multimodal LLM | 2023 | [link](https://proceedings.mlr.press/v235/wu24e.html) | [link](https://next-gpt.github.io/) |
| Video-LLaMA | Video-LLaMA: An Instruction-tuned Audio-Visual Language Model for Video Understanding | 2023 | [link](https://aclanthology.org/2023.emnlp-demo.49/) | [link](https://github.com/DAMO-NLP-SG/Video-LLaMA) |
| Video-LLaMA2 | VideoLLaMA 2: Advancing Spatial-Temporal Modeling and Audio Understanding in Video-LLMs | 2024 | [link](https://arxiv.org/abs/2406.07476) | [link](https://github.com/DAMO-NLP-SG/VideoLLaMA2) |
| Video-SALMONN | video-salmonn: Speech-enhanced audio-visual large language models | 2024 | [link](https://proceedings.mlr.press/v235/sun24l.html) | [link](https://github.com/bytedance/SALMONN/) |
| Gemini Pro | Gemini: a family of highly capable multimodal models | 2023 | [link](https://arxiv.org/abs/2312.11805) | NA |
| LLaMA 3 | The llama 3 herd of models | 2024 | [link](https://arxiv.org/abs/2407.21783) | [link](https://github.com/meta-llama/llama3) |
| Qwen2.5-Omni | Qwen2. 5-omni technical report | 2025 | [link](https://arxiv.org/abs/2503.20215) | [link](https://github.com/QwenLM/Qwen2.5-Omni) |
| GPT-4o | GPT-4o System Card | 2024 | [link](https://arxiv.org/abs/2410.21276) | NA |




## 🔥 Applications of Foundation Models in Biometrics
In this section, we review recent papers on the applications of foundation models in biometrics:

- [Foundation Models for Biometric Recognition](#foundation-models-for-biometric-recognition)
- [Foundation Models for Soft-biometric Detection](#foundation-models-for-soft-biometric-detection)
- [Foundation Models for Deepfake and Forgery Detection](#foundation-models-for-deepfake-and-forgery-detection)
- [Foundation Models for Anti-spoofing](#foundation-models-for-anti-spoofing)
- [Foundation Models for Synthetic Biometric Generation](#foundation-models-for-synthetic-biometric-generation)

### Foundation Models for Biometric Recognition

| Paper Title | Year | Modality / Task | Paper | Code |
|---|---|---|---|---|
| Exploring wav2vec 2.0 on speaker verification and language identification | 2020 | speaker and language identification | [link](https://arxiv.org/abs/2012.06185) | NA |
| ChatGPT and biometrics: an assessment of face recognition, gender detection, and age estimation capabilities | 2024 | face verification, gender detection, age estimation | [link](https://arxiv.org/abs/2403.02965) | NA |
| How Good is ChatGPT at Face Biometrics? A First Look into Recognition, Soft Biometrics, and Explainability | 2024 | face verification | [link](https://ieeexplore.ieee.org/abstract/document/10445251/) | NA |
| ChatGPT Meets Iris Biometrics | 2024 | iris recognition | [link](https://arxiv.org/abs/2408.04868) | NA |
| Foundation versus Domain-specific Models: Performance Comparison, Fusion, and Explainability in Face Recognition | 2025 | face verification | [link](https://openaccess.thecvf.com/content/ICCV2025W/FoundGen-Bio/html/Sony_Foundation_versus_Domain-specific_Models_Performance_Comparison_Fusion_and_Explainability_in_ICCVW_2025_paper.html) | NA |
| Benchmarking Foundation Models for Zero-Shot Biometric Tasks | 2025 | face verification, soft biometric attribute prediction (gender and race), iris recognition, iris presentation attack detection, face morph detection, and face deepfake detection | [link](https://arxiv.org/abs/2505.24214) | NA |
| A fine-tuned wav2vec 2.0/hubert benchmark for speech emotion recognition, speaker verification and spoken language understanding | 2021 | speaker verification | [link](https://arxiv.org/abs/2111.02735) | [link](https://github.com/speechbrain/speechbrain/tree/develop/recipes) |
| Iris-SAM: Iris Segmentation Using a Foundation Model | 2024 | iris segmentation | [link](https://arxiv.org/abs/2402.06497) | [link](https://github.com/ParisaFarmanifard/Iris-SAM) |
| SAM-Iris: A SAM-Based Iris Segmentation Algorithm | 2025 | iris segmentation | [link](https://www.mdpi.com/2079-9292/14/2/246) | NA |
| Froundation: Are foundation models ready for face recognition? | 2024 | face recognition | [link](https://www.sciencedirect.com/science/article/pii/S0262885625000411) | [link](https://github.com/TaharChettaoui/FRoundation) |
| HumanOmni: A Large Vision-Speech Language Model for Human-Centric Video Understanding | 2025 | audio-visual human video recognition (emotion recognition, expression description, and action understanding) | [link](https://arxiv.org/abs/2501.15111) | [link](https://github.com/HumanMLLM/HumanOmni) |
| FaceLLM: A Multimodal Large Language Model for Face Understanding | 2025 | face recognition, anti-spoofing, deepfake detection, attribute prediction, expression, parsing, pose, crowd counting | [link](https://openaccess.thecvf.com/content/ICCV2025W/FoundGen-Bio/html/Shahreza_FaceLLM_A_Multimodal_Large_Language_Model_for_Face_Understanding_ICCVW_2025_paper.html) | [link](https://www.idiap.ch/paper/facellm/) |
| FaceXBench: Evaluating Multimodal LLMs on Face Understanding | 2025 | face recognition, anti-spoofing, deepfake detection, attribute prediction, expression, parsing, pose, crowd counting | [link](https://arxiv.org/abs/2501.10360) | [link](https://github.com/Kartik-3004/facexbench) |
| Face-Human-Bench: A Comprehensive Benchmark of Face and Human Understanding for Multi-modal Assistants | 2025 | facial attributes, age estimation, expression recognition, attack detection, recognition; human attributes, action, spatial/social relations, re-ID | [link](https://arxiv.org/abs/2501.01243) | [link](https://face-human-bench.github.io/) |
| From Pixels to Words: Leveraging Explainability in Face Recognition through Interactive Natural Language Processing | 2024 | face recognition explainability | [link](https://arxiv.org/abs/2409.16089) | NA |
| FaceOracle: Chat with a Face Image Oracle | 2025 | face image quality assessment | [link](https://arxiv.org/abs/2501.07202) | NA |
| Unispeech-sat: Universal speech representation learning with speaker aware pre-training | 2022 | speaker ID, verification, diarization, phoneme recognition, keyword spotting, emotion recognition | [link](https://arxiv.org/abs/2110.05752) | [link](https://github.com/microsoft/UniSpeech) |
| Large-scale self-supervised speech representation learning for automatic speaker verification | 2022 | speaker verification | [link](https://arxiv.org/abs/2110.05777) | [link](https://github.com/microsoft/UniSpeech) |
| General facial representation learning in a visual-linguistic manner | 2022 | face parsing, alignment, attribute recognition | [link](https://openaccess.thecvf.com/content/CVPR2022/html/Zheng_General_Facial_Representation_Learning_in_a_Visual-Linguistic_Manner_CVPR_2022_paper.html) | [link](https://github.com/faceperceiver/farl) |
| Marlin: Masked autoencoder for facial video representation learning | 2023 | face attribute recognition, expression recognition, deepfake detection, lip synchronization | [link](https://openaccess.thecvf.com/content/CVPR2023/html/Cai_MARLIN_Masked_Autoencoder_for_Facial_Video_Representation_LearnINg_CVPR_2023_paper.html) | [link](https://github.com/ControlNet/MARLIN) |
| Self-Supervised Facial Representation Learning with Facial Region Awareness | 2024 | face expression and attribute recognition | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Gao_Self-Supervised_Facial_Representation_Learning_with_Facial_Region_Awareness_CVPR_2024_paper.html) | [link](https://github.com/zaczgao/Facial_Region_Awareness) |
| Pose-disentangled contrastive learning for self-supervised facial representation | 2023 | face expression, face recognition, head pose estimation | [link](https://openaccess.thecvf.com/content/CVPR2023/html/Liu_Pose-Disentangled_Contrastive_Learning_for_Self-Supervised_Facial_Representation_CVPR_2023_paper.html) | [link](https://github.com/DreamMr/PCL) |
| Pros: Facial omni-representation learning via prototype-based self-distillation | 2024 | face parsing, attribute recognition, emotion detection, landmark detection | [link](https://openaccess.thecvf.com/content/WACV2024/html/Di_ProS_Facial_Omni-Representation_Learning_via_Prototype-Based_Self-Distillation_WACV_2024_paper.html) | [link](https://github.com/1adrianb/unsupervised-face-representation) |
| ComFace: Facial Representation Learning with Synthetic Data for Comparing Faces | 2024 | face expression change, weight change, age change estimation | [link](https://arxiv.org/abs/2405.16016) | NA |
| SwinFace: a multi-task transformer for face recognition, expression recognition, age estimation and attribute estimation | 2023 | face attributes, age estimation,  expression recognition, face recognition | [link](https://arxiv.org/abs/2308.11509) | [link](https://github.com/lxq1000/SwinFace) |
| FaceXFormer: A Unified Transformer for Facial Analysis | 2024 | face parsing, landmarks, head pose estimation, age/gender/race estimation, attribute recognition, expression recognition, | [link](https://openaccess.thecvf.com/content/ICCV2025/html/Narayan_FaceXFormer_A_Unified_Transformer_for_Facial_Analysis_ICCV_2025_paper.html) | [link](https://github.com/Kartik-3004/facexformer) |
| Task-adaptive Q-Face | 2024 | head pose estimation, face attribute recognition, age estimation, expression recognition | [link](https://arxiv.org/abs/2405.09059) | NA |
| Faceptor: A generalist model for face perception | 2024 | face parsing, landmarks,  age and gender estimation, attribute recognition, expression recognition, face recognition | [link](https://arxiv.org/abs/2403.09500) | [link](https://github.com/lxq1000/Faceptor) |


### Foundation Models for Soft-biometric Detection

| Paper Title | Year | Modality / Task | Paper | Code |
|---|---|---|---|---|
| Robust light-weight facial affective behavior recognition with clip | 2024 | facial expression classification; action unit detection | [link](https://arxiv.org/abs/2403.09915) | [link](https://github.com/Purdue-M2/Affective_Behavior_Analysis_M2_PURDUE) |
| Cliper: A unified vision-language framework for in-the-wild facial expression recognition | 2024 | face static & dynamic expression recognition | [link](https://arxiv.org/abs/2303.00193) | [link](https://github.com/muse1998/CLIPER) |
| Emoclip: A vision-language method for zero-shot video facial expression recognition | 2024 | video facial emotion recognition | [link](https://arxiv.org/abs/2310.16640) | [link](https://github.com/NickyFot/EmoCLIP) |
| Finecliper: Multi-modal fine-grained clip for dynamic facial expression recognition with adapters | 2024 | dynamic facial expression recognition | [link](https://arxiv.org/abs/2407.02157) | NA |
| Face-mllm: A large face perception model | 2024 | face age/gender, expression, action units, attributes | [link](https://arxiv.org/abs/2410.20717) | NA |
| FaceGPT: Self-supervised Learning to Chat about 3D Human Faces | 2024 | face 3DMM parameter generation | [link](https://arxiv.org/abs/2406.07163) | NA |
| FaceBench: A Multi-View Multi-Level Facial Attribute VQA Dataset for Benchmarking Face Perception MLLMs | 2025 | face attribute detection | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_FaceBench_A_Multi-View_Multi-Level_Facial_Attribute_VQA_Dataset_for_Benchmarking_CVPR_2025_paper.html) | [link](https://github.com/CVI-SZU/FaceBench) |
| Face-LLaVA: Facial Expression and Attribute Understanding through Instruction Tuning | 2025 | face expression recognition, action unit detection, facial attribute detection, age estimation, and deepfake detection | [link](https://openaccess.thecvf.com/content/WACV2026/html/Chaubey_Face-LLaVA_Facial_Expression_and_Attribute_Understanding_through_Instruction_Tuning_WACV_2026_paper.html) | [link](https://github.com/ihp-lab/Face-LLaVA/) |
| FaceInsight: A Multimodal Large Language Model for Face Perception | 2025 | face attribute recognition, age/ gender/ race estimation, and expression prediction | [link](https://arxiv.org/abs/2504.15624) | NA |
| R1-omni: Explainable omni-multimodal emotion recognition with reinforcement learning | 2025 | audio-visual emotion recognition with reasoning | [link](https://arxiv.org/abs/2503.05379) | [link](https://github.com/HumanMLLM/R1-Omni) |
| ChatGPT and biometrics: an assessment of face recognition, gender detection, and age estimation capabilities | 2024 | face gender detection, age estimation | [link](https://arxiv.org/abs/2403.02965) | NA |
| How Good is ChatGPT at Face Biometrics? A First Look into Recognition, Soft Biometrics, and Explainability | 2024 | age, gender, ethnicity, hair color | [link](https://arxiv.org/abs/2401.13641) | NA |
| ChatGPT Meets Iris Biometrics | 2024 | iris–face matching; soft-biometrics | [link](https://arxiv.org/abs/2408.04868) | NA |


### Foundation Models for Deepfake and Forgery Detection

| Paper Title | Year | Modality / Task | Paper | Code |
|---|---|---|---|---|
| MFCLIP: Multi-modal Fine-grained CLIP for Generalizable Diffusion Face Forgery Detection | 2024 | face forgery detection | [link](https://arxiv.org/abs/2409.09724) | [link](https://github.com/Jenine-321/MFCLIP) |
| Forensics Adapter: Adapting CLIP for Generalizable Face Forgery Detection | 2024 | face forgery detection | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Cui_Forensics_Adapter_Adapting_CLIP_for_Generalizable_Face_Forgery_Detection_CVPR_2025_paper.html) | [link](https://github.com/OUC-VAS/ForensicsAdapter) |
| MADation: Face Morphing Attack Detection with Foundation Models | 2025 | face morph attack detection | [link](https://openaccess.thecvf.com/content/WACV2025W/MAPA/html/Caldeira_MADation_Face_Morphing_Attack_Detection_with_Foundation_Models_WACVW_2025_paper.html) | [link](https://github.com/gurayozgur/MADation) |
| FSFM: A Generalizable Face Security Foundation Model via Self-Supervised Facial Representation Learning | 2024 | deepfake detection, anti-spoofing, unseen diffusion forgery | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_FSFM_A_Generalizable_Face_Security_Foundation_Model_via_Self-Supervised_Facial_CVPR_2025_paper.html) | [link](https://fsfm-3c.github.io/) |
| Automatic speaker verification spoofing and deepfake detection using wav2vec 2.0 and data augmentation | 2022 | voice spoofing & deepfake detection | [link](https://arxiv.org/abs/2202.12233) | [link](https://github.com/TakHemlata/SSL_Anti-spoofing) |
| X2-dfd: A framework for explainable and extendable deepfake detection | 2024 | face deepfake detection | [link](https://arxiv.org/abs/2410.06126) | [link](https://github.com/chenyize111/X2DFD) |
| Ffaa: Multimodal large language model based explainable open-world face forgery analysis assistant | 2024 | forgery analysis assistant | [link](https://arxiv.org/abs/2408.10072) | [link](https://ffaa-vl.github.io/) |
| Towards general visual-linguistic face forgery detection (v2) | 2025 | face forgery detection | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Sun_Towards_General_Visual-Linguistic_Face_Forgery_Detection_CVPR_2025_paper.html) | [link](https://github.com/skJack/VLFFD) |
| Evaluating the Effectiveness of Attack-Agnostic Features for Morphing Attack Detection | 2024 | face morph attack detection | [link](https://arxiv.org/abs/2410.16802) | [link](https://gitlab.idiap.ch/bob/bob.paper.ijcb2024_agnostic_features_mad) |
| Are Music Foundation Models Better at Singing Voice Deepfake Detection? Far-Better Fuse them with Speech Foundation Models | 2024 | speaker deepfake detection | [link](https://arxiv.org/abs/2409.14131) | NA |
| Rethinking Vision-Language Model in Face Forensics: Multi-Modal Interpretable Forged Face Detector | 2025 | face deepfake detection \newline+ description | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Guo_Rethinking_Vision-Language_Model_in_Face_Forensics_Multi-Modal_Interpretable_Forged_Face_CVPR_2025_paper.html) | [link](https://github.com/CHELSEA234/M2F2_Det) |
| Standing on the shoulders of giants: Reprogramming visual-language model for general deepfake detection | 2025 | face deepfake detection | [link](https://ojs.aaai.org/index.php/AAAI/article/view/32559) | [link](https://github.com/KQL11/RepDFD) |
| Can chatgpt detect deepfakes? a study of using multimodal large language models for media forensics | 2024 | face deepfake detection | [link](https://openaccess.thecvf.com/content/CVPR2024W/WMF/html/Jia_Can_ChatGPT_Detect_DeepFakes_A_Study_of_Using_Multimodal_Large_CVPRW_2024_paper.html) | [link](https://github.com/shanface33/GPT4MF_UB) |
| How Good is ChatGPT at Audiovisual Deepfake Detection: A Comparative Study of ChatGPT, AI Models and Human Perception | 2024 | audio-visual deepfake detection | [link](https://arxiv.org/abs/2411.09266) | NA |
| ChatGPT Encounters Morphing Attack Detection: Zero-Shot MAD with Multi-Modal Large Language Models and General Vision Models | 2025 | face morph detection | [link](https://arxiv.org/abs/2503.10937) | NA |


### Foundation Models for Anti-spoofing

| Paper Title | Year | Modality / Task | Paper | Code |
|---|---|---|---|---|
| Flip: Cross-domain face anti-spoofing with language guidance | 2023 | fine‐tune CLIP image encoder for face (FLIP alignment) | [link](https://openaccess.thecvf.com/content/ICCV2023/html/Srivatsan_FLIP_Cross-domain_Face_Anti-spoofing_with_Language_Guidance_ICCV_2023_paper.html) | [link](https://github.com/koushiksrivats/FLIP) |
| On Self-Supervised Learning and Prompt Tuning of Vision Transformers for Cross-sensor Fingerprint Presentation Attack Detection | 2023 | SSL via masked‐fingerprint prediction with prompt tuning  | [link](https://ieeexplore.ieee.org/abstract/document/10448619) | NA |
| CPL-CLIP: Compound Prompt Learning for Flexible-Modal Face Anti-Spoofing | 2024 | face anti-spoofing | [link](https://ieeexplore.ieee.org/abstract/document/10744492) | NA |
| Fm-clip: Flexible modal clip for face anti-spoofing | 2024 | cross‐modal antispoofing  | [link](https://dl.acm.org/doi/abs/10.1145/3664647.3680856) | NA |
| La-SoftMoE CLIP for Unified Physical-Digital Face Attack Detection | 2024 | Unified physical-digital face attack detection | [link](https://arxiv.org/abs/2408.12793) | NA |
| Cfpl-fas: Class free prompt learning for generalizable face anti-spoofing | 2024 | face anti-spoofing | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Liu_CFPL-FAS_Class_Free_Prompt_Learning_for_Generalizable_Face_Anti-spoofing_CVPR_2024_paper.html) | NA |
| InstructFLIP: Exploring Unified Vision-Language Model for Face Anti-spoofing | 2025 | face anti-spoofing | [link](https://dl.acm.org/doi/abs/10.1145/3746027.3754939) | [link](https://kunkunlin1221.github.io/InstructFLIP/) |
| Reliable and Balanced Transfer Learning for Generalized Multimodal Face Anti-Spoofing | 2025 | Multimodal face anti-spoofing | [link](https://ieeexplore.ieee.org/abstract/document/11015656/) | [link](https://github.com/lxbuaa/mmdg_plus_plus) |
| FaceShield: Explainable Face Anti-Spoofing with Multimodal Large Language Models | 2025 | face anti-spoofing (classification and attack localization) | [link](https://ojs.aaai.org/index.php/AAAI/article/view/37945) | [link](https://github.com/Why0912/FaceShield) |
| Interpretable face anti-spoofing: Enhancing generalization with multimodal large language models | 2025 | face anti-spoofing | [link](https://ojs.aaai.org/index.php/AAAI/article/view/33073) | NA |
| Exploring Task-Solving Paradigm for Generalized Cross-Domain Face Anti-Spoofing via Reinforcement Fine-Tuning | 2025 | face anti-spoofing (spoofing detection and reasoning) | [link](https://arxiv.org/abs/2506.21895) | NA |
| VL-FAS: Domain Generalization via Vision-Language Model For Face Anti-Spoofing | 2024 | face anti‐spoofing | [link](https://ieeexplore.ieee.org/abstract/document/10448156/) | NA |
| FoundPAD: Foundation Models Reloaded for Face Presentation Attack Detection | 2025 | face anti‐spoofing | [link](https://openaccess.thecvf.com/content/WACV2025W/AI4MFDD/html/Ozgur_FoundPAD_Foundation_Models_Reloaded_for_Face_Presentation_Attack_Detection_WACVW_2025_paper.html) | [link](https://github.com/gurayozgur/FoundPAD) |
| Towards Iris Presentation Attack Detection with Foundation Models | 2025 | iris anti‐spoofing | [link](https://arxiv.org/abs/2501.06312) | NA |
| Exploring ChatGPT for Face Presentation Attack Detection in Zero and Few-Shot in-Context Learning | 2025 | face presentation attack detection | [link](https://openaccess.thecvf.com/content/WACV2025W/RWS/html/Komaty_Exploring_ChatGPT_for_Face_Presentation_Attack_Detection_in_Zero_and_WACVW_2025_paper.html) | [link](https://gitlab.idiap.ch/bob/bob.paper.wacv2025_chatgpt_face_pad) |
| Are Foundation Models All You Need for Zero-shot Face Presentation Attack Detection? | 2025 | face presentation attack detection | [link](https://arxiv.org/abs/2507.16393) | [link](https://github.com/ljsoler/zero-shot-FoundationPAD) |
| Shield: An evaluation benchmark for face spoofing and forgery detection with multimodal large language models | 2025 | face anti-spoofing (RGB, infrared, depth) and forgery detection | [link](https://link.springer.com/article/10.1007/s44267-025-00079-w) | [link](https://github.com/laiyingxin2/SHIELD) |
| ChatGPT Meets Iris Biometrics | 2024 | iris presentation‐attack detection | [link](https://arxiv.org/abs/2408.04868) | NA |


### Foundation Models for Synthetic Biometric Generation

| Paper Title | Year | Modality / Task | Paper | Code |
|---|---|---|---|---|
| Toward open-world text-driven face generation and manipulation via stylegan3 | 2024 | Text-to-face synthesis | [link](https://ieeexplore.ieee.org/document/10620351) | NA |
| AnyFace++: A unified framework for free-style text-to-face synthesis and manipulation | 2024 | Text-guided face editing  | [link](https://ui.adsabs.harvard.edu/abs/2025ITPAM..47.9438S/abstract) | NA |
| AnyFace: Free-style text-to-face synthesis and manipulation | 2022 | Text-to-face generation | [link](https://openaccess.thecvf.com/content/CVPR2022/html/Sun_AnyFace_Free-Style_Text-To-Face_Synthesis_and_Manipulation_CVPR_2022_paper.html) | NA |
| Towards counterfactual image manipulation via clip | 2022 | Controllable text-to-face | [link](https://dl.acm.org/doi/abs/10.1145/3503161.3547935) | [link](https://github.com/yingchen001/CF-CLIP) |
| Prompt-Based Modality Bridging for Unified Text-to-Face Generation and Manipulation | 2024 | Prompt-based face synthesis  | [link](https://dl.acm.org/doi/full/10.1145/3694974) | NA |
| Tecm-clip: Text-based controllable multi-attribute face image manipulation | 2022 | face attribute / expression editing | [link](https://openaccess.thecvf.com/content/ACCV2022/html/Lou_TeCM-CLIP_Text-based_Controllable_Multi-attribute_Face_Image_Manipulation_ACCV_2022_paper.html) | [link](https://github.com/lxd941213/TeCM-CLIP) |
| Stylemc: Multi-channel based fast text-guided image generation and manipulation | 2022 | face multi-attribute editing | [link](https://openaccess.thecvf.com/content/WACV2022/html/Kocasari_StyleMC_Multi-Channel_Based_Fast_Text-Guided_Image_Generation_and_Manipulation_WACV_2022_paper.html) | [link](https://catlab-team.github.io/stylemc/) |
| Photoverse: Tuning-free image customization with text-to-image diffusion models | 2023 | Few-shot personalised face portrait generation | [link](https://arxiv.org/abs/2309.05793) | [link](https://github.com/idonahum/photoVerse) |
| Fastcomposer: Tuning-free multi-subject image generation with localized attention | 2024 | fast subject-driven face text-to-image | [link](https://link.springer.com/article/10.1007/s11263-024-02227-z) | [link](https://github.com/mit-han-lab/fastcomposer) |
| Moa: Mixture-of-attention for subject-context disentanglement in personalized image generation | 2024 | multi-concept face portrait generation | [link](https://dl.acm.org/doi/full/10.1145/3680528.3687662) | NA |
| Photomaker: Customizing realistic human photos via stacked id embedding | 2024 | high-fidelity face personalisation | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Li_PhotoMaker_Customizing_Realistic_Human_Photos_via_Stacked_ID_Embedding_CVPR_2024_paper.html) | [link](https://photo-maker.github.io/) |
| Face0: Instantaneously conditioning a text-to-image model on a face | 2023 | Identity-preserving face text-to-image | [link](https://dl.acm.org/doi/abs/10.1145/3610548.3618249) | NA |
| Ip-adapter: Text compatible image prompt adapter for text-to-image diffusion models | 2023 | face instant personalisation | [link](https://arxiv.org/abs/2308.06721) | [link](https://ip-adapter.github.io/) |
| Dreamidentity: Improved editability for efficient face-identity preserved image generation | 2023 | face identity-guided generation | [link](http://ojs.aaai.org/index.php/AAAI/article/view/27891) | NA |
| Portraitbooth: A versatile portrait model for fast identity-preserved personalization | 2024 | face few-shot portrait generation | [link](https://openaccess.thecvf.com/content/CVPR2024/html/Peng_PortraitBooth_A_Versatile_Portrait_Model_for_Fast_Identity-preserved_Personalization_CVPR_2024_paper.html) | NA |
| Instantid: Zero-shot identity-preserving generation in seconds | 2024 | face real-time personalisation | [link](https://arxiv.org/abs/2401.07519) | [link](https://github.com/instantX-research/InstantID) |
| ID-Aligner: Enhancing Identity-Preserving Text-to-Image Generation with Reward Feedback Learning | 2024 | face identity-consistent generation | [link](https://arxiv.org/abs/2404.15449) | [link](https://github.com/Weifeng-Chen/ID-Aligner) |
| Facestudio: Put your face everywhere in seconds | 2023 | face ID & style controllable text-to-image | [link](https://arxiv.org/abs/2312.02663) | [link](icoz69.github.io/facestudio/) |
| IDAdapter: Learning Mixed Features for Tuning-Free Personalization of Text-to-Image Models | 2024 | identity-aware face editing | [link](https://openaccess.thecvf.com/content/CVPR2024W/FAS2024/html/Cui_IDAdapter_Learning_Mixed_Features_for_Tuning-Free_Personalization_of_Text-to-Image_Models_CVPRW_2024_paper.html) | NA |
| Arc2face: A foundation model for id-consistent human faces | 2024 | identity-conditioned face generation | [link](https://link.springer.com/chapter/10.1007/978-3-031-72913-3_14) | [link](https://github.com/foivospar/Arc2Face) |
| Face Reconstruction from Face Embeddings using Adapter to a Face Foundation Model | 2024 | General identity-conditioned face generation | [link](https://openaccess.thecvf.com/content/CVPR2025W/ABAW/html/Shahreza_Face_Reconstruction_from_Face_Embeddings_using_Adapter_to_a_Face_CVPRW_2025_paper.html) | [link](https://www.idiap.ch/paper/face_adapter/) |
| Arc2Avatar: Generating Expressive 3D Avatars from a Single Image via ID Guidance | 2025 | Identity-conditioned 3D head / avatar generation | [link](https://openaccess.thecvf.com/content/CVPR2025/html/Gerogiannis_Arc2Avatar_Generating_Expressive_3D_Avatars_from_a_Single_Image_via_CVPR_2025_paper.html) | [link](https://arc2avatar.github.io/) |
| ClipSwap: Towards High Fidelity Face Swapping via Attributes and CLIP-Informed Loss | 2024 | Face swapping | [link](https://ieeexplore.ieee.org/abstract/document/10581924) | NA |



## 📚 Missing Papers

We will keep updating the [git repository](https://github.com/otroshi/foundation-models-biometrics) and [webpage](https://otroshi.github.io/foundation-models-biometrics/) of our survey. Please contact the first author (hatef.otroshi@idiap.ch) or complete the following form to add your paper:

👉 [Submit Your Paper](https://forms.gle/NYNjhEKg6q4Pn1UM7)

We appreciate your contributions and look forward to keeping this survey comprehensive and up to date!


## ©️ Citation
If you find this survey useful, please consider citing it:

```bibtex
@article{fmbiometrics2025survey,
  title={Foundation Models and Biometrics: A Survey and Outlook},
  author={Hatef Otroshi Shahreza and S{\'e}bastien Marcel},
  journal={IEEE Transactions on Information Forensics and Security},
  year={2025},
  publisher={IEEE}
}
```