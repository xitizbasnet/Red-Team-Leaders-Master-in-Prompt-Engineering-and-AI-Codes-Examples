# AI Terminology Glossary

## Module 01 - Foundations of Artificial Intelligence
### Complete Reference of Terms Used in This Module

---

## A

**AGI (Artificial General Intelligence)**
A hypothetical AI system that can understand, learn, and apply intelligence across any intellectual task that a human can perform. AGI does not yet exist. Also called "Strong AI."

**AI (Artificial Intelligence)**
The field of computer science dedicated to creating systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, perception, and language understanding.

**AI Alignment**
The challenge of ensuring that AI systems' goals and behaviors are aligned with human values and intentions. A major focus of AI safety research.

**AI Winter**
A period of reduced funding, interest, and progress in AI research. Two major AI winters occurred: 1974-1980 and 1987-1993.

**ANI (Artificial Narrow Intelligence)**
AI systems designed to perform specific tasks or a narrow set of related tasks. All current AI systems, including ChatGPT and Claude, are classified as ANI. Also called "Weak AI."

**API (Application Programming Interface)**
A set of protocols and tools that allows different software applications to communicate. In AI, APIs allow developers to send prompts to models and receive generated responses.

**ASI (Artificial Super Intelligence)**
A hypothetical form of AI that surpasses human intelligence in every domain. ASI is currently theoretical and the subject of significant debate.

**Attention Mechanism**
A technique in neural networks that allows the model to focus on relevant parts of the input when producing output. The self-attention mechanism is the core innovation of the Transformer architecture.

**Autoregressive Model**
A model that generates output one token at a time, where each new token is conditioned on all previously generated tokens. GPT and Claude are autoregressive models.

---

## B

**Backpropagation**
The algorithm used to train neural networks by calculating gradients of the loss function with respect to each weight. It propagates error signals backward through the network to update weights.

**Batch Processing**
Processing multiple API requests together rather than one at a time. Often offered at reduced pricing by API providers.

**Benchmark**
A standardized test used to evaluate and compare AI model performance. Examples: MMLU, HumanEval, GPQA, MT-Bench.

**BERT (Bidirectional Encoder Representations from Transformers)**
A language model by Google (2018) that processes text bidirectionally. Primarily used for understanding tasks (classification, question answering) rather than generation.

**BPE (Byte-Pair Encoding)**
The most common tokenization algorithm used by modern LLMs. It iteratively merges the most frequent character pairs to build a vocabulary of subword tokens.

**Bias (in AI)**
Systematic and unfair patterns in AI outputs that reflect biases present in training data or design choices. Can lead to discriminatory or skewed results.

---

## C

**Chain-of-Thought (CoT) Prompting**
A technique where the model is instructed to reason step by step before giving a final answer. Improves performance on complex reasoning tasks.

**Chatbot**
An AI application designed for conversational interaction with humans. Examples: ChatGPT, Claude.ai, Gemini.

**Classification**
A machine learning task where the model assigns input data to predefined categories. Example: spam detection (spam vs. not spam).

**CLIP (Contrastive Language-Image Pre-training)**
A model by OpenAI that understands the relationship between text and images. Used as the text encoder in many image generation systems.

**Closed-Source Model**
An AI model where the weights, training code, and training data are not publicly released. Accessible only via API. Examples: GPT-4, Claude.

**CNN (Convolutional Neural Network)**
A type of neural network specialized for processing grid-like data such as images. Uses convolutional filters to detect patterns like edges, shapes, and objects.

**Constitutional AI**
An approach developed by Anthropic for training AI models using a set of principles (a "constitution") rather than relying solely on human feedback. Used to train Claude.

**Context Window**
The maximum number of tokens a model can process in a single interaction, including both input and output. Ranges from 4K to 1M+ tokens across different models.

**ControlNet**
A neural network extension for diffusion models (like Stable Diffusion) that adds spatial control to the generation process using reference images (edges, depth maps, poses, etc.).

---

## D

**DALL-E**
An image generation model by OpenAI. DALL-E 3 (2023) generates images from text descriptions using diffusion model technology.

**Deep Learning**
A subset of machine learning that uses neural networks with many layers (hence "deep") to learn hierarchical representations of data. Foundation of modern AI.

**DeepSeek**
A Chinese AI company that produces efficient, high-performance open-weight language models. DeepSeek-V3 and DeepSeek-R1 are notable models.

**Diffusion Model**
A type of generative model that creates data (images, audio, video) by learning to reverse a gradual noising process. Start with noise, progressively denoise to produce output.

**Discriminative Model**
A model that classifies or distinguishes between categories of existing data (e.g., spam vs. not spam). Contrast with generative models that create new data.

---

## E

**ElevenLabs**
A leading AI voice synthesis company offering text-to-speech, voice cloning, and audio AI tools.

**Embedding**
A numerical vector representation of data (text, images, etc.) in a high-dimensional space. Similar items have similar embeddings, enabling semantic search and comparison.

**Emergent Abilities**
Capabilities that appear in large AI models but are absent in smaller ones. Not explicitly trained for but emerge from scale. Examples: in-context learning, chain-of-thought reasoning.

**Encoder-Decoder**
A neural network architecture where an encoder processes input into a latent representation and a decoder generates output from that representation. Used in translation and summarization.

**Epoch**
One complete pass through the entire training dataset during model training. Models are typically trained for multiple epochs.

---

## F

**Few-Shot Learning**
A technique where a model learns to perform a task from just a few examples provided in the prompt. Contrast with zero-shot (no examples) and fine-tuning (many examples).

**Fine-Tuning**
The process of further training a pre-trained model on a specific dataset to adapt it for a particular task or domain. More targeted than pre-training.

**Flux**
An image generation model by Black Forest Labs (founded by original Stable Diffusion researchers). Uses a transformer-based architecture with flow matching.

**Foundation Model**
A large AI model trained on broad data that can be adapted to many downstream tasks. Examples: GPT-4, Claude, LLaMA.

---

## G

**GAN (Generative Adversarial Network)**
A generative model architecture where two networks compete: a generator creates fake data and a discriminator tries to distinguish real from fake. Invented by Ian Goodfellow in 2014.

**Gemini**
Google DeepMind's family of multimodal AI models. Includes Gemini Ultra, Pro, and Flash variants.

**Generative AI**
AI systems that create new content (text, images, audio, video, code) rather than just analyzing or classifying existing data.

**GPT (Generative Pre-trained Transformer)**
A family of language models by OpenAI. "Generative" (creates text), "Pre-trained" (trained on large data), "Transformer" (architecture used).

**GPU (Graphics Processing Unit)**
Hardware originally designed for rendering graphics but now essential for training and running AI models due to its parallel processing capabilities. NVIDIA GPUs dominate AI computing.

**Gradient Descent**
An optimization algorithm used to minimize the loss function during training by iteratively adjusting model weights in the direction that reduces error.

**Grounding**
Connecting AI models to real-world data sources (databases, search engines, documents) to improve accuracy and reduce hallucinations.

---

## H

**Hallucination**
When an AI model generates information that is factually incorrect, fabricated, or not supported by its training data, while presenting it confidently as fact.

**HuggingFace**
The largest platform for sharing, discovering, and deploying machine learning models. Hosts 500,000+ models and provides the widely-used Transformers library.

**Hyperparameter**
A configuration setting for the training process that is set before training begins (e.g., learning rate, batch size, number of layers). Contrast with parameters, which are learned during training.

---

## I

**Image-to-Image (img2img)**
An AI technique that transforms an existing image based on a text prompt, rather than generating from scratch. Used for style transfer, modification, and enhancement.

**In-Context Learning**
The ability of large language models to learn from examples provided within the prompt, without any weight updates or fine-tuning. An emergent ability of large models.

**Inference**
The process of using a trained model to generate predictions or outputs from new inputs. Contrast with training (the process of learning from data).

**Inpainting**
An AI technique for filling in or replacing specific parts of an image, guided by a mask and text prompt.

**Instruction Tuning**
Training a model to follow instructions by providing examples of instruction-response pairs. A key step in making raw language models useful as assistants.

---

## K

**Knowledge Cutoff**
The date beyond which a model has no training data. Models trained with data up to a specific date cannot know about events that occurred after that date (without retrieval augmentation).

---

## L

**LangChain**
A popular framework for building applications powered by language models. Provides tools for chaining LLM calls, managing memory, and connecting to external data sources.

**Latent Space**
A compressed, mathematical representation of data learned by a model. Operations in latent space are more efficient than in the original data space.

**LLM (Large Language Model)**
A language model with billions of parameters, trained on vast amounts of text data. Examples: GPT-4, Claude, Gemini, LLaMA.

**LLaMA (Large Language Model Meta AI)**
Meta's family of open-weight language models. LLaMA 3.1 is available in 8B, 70B, and 405B parameter sizes.

**LoRA (Low-Rank Adaptation)**
A parameter-efficient fine-tuning technique that adds small trainable matrices to a pre-trained model. Enables customization with much less data and compute than full fine-tuning.

**Loss Function**
A mathematical function that measures how wrong a model's predictions are. Training aims to minimize this function. Common examples: cross-entropy loss, MSE.

---

## M

**Machine Learning (ML)**
A subset of AI where systems learn patterns from data rather than being explicitly programmed. Includes supervised, unsupervised, and reinforcement learning.

**Midjourney**
An AI image generation platform known for producing the highest aesthetic quality images. Accessed primarily through Discord.

**Mistral AI**
A French AI company building efficient language models. Known for Mistral and Mixtral models.

**MoE (Mixture of Experts)**
An architecture where a model contains multiple specialized sub-networks ("experts") and a router selects which experts to activate for each input. Enables larger total parameters with efficient inference.

**Multi-Head Attention**
A Transformer component that runs multiple attention operations in parallel, each focusing on different types of relationships in the data.

**Multimodal**
AI models that can process and/or generate multiple types of data (text, images, audio, video) within a single system. Examples: GPT-4o, Gemini.

---

## N

**Natural Language Processing (NLP)**
A branch of AI focused on enabling computers to understand, interpret, and generate human language.

**Neural Network**
A computational model inspired by the structure of biological neurons. Consists of layers of interconnected nodes that process information.

**Next-Token Prediction**
The core training objective of autoregressive language models: given a sequence of tokens, predict the probability distribution over possible next tokens.

**Noise (in Diffusion Models)**
Random data added to or removed from an image during the diffusion process. Training teaches the model to predict and remove noise, generating coherent outputs.

---

## O

**Open-Source Model**
An AI model where the weights (and sometimes training code and data) are publicly available. Anyone can download, run, modify, and deploy these models. Examples: LLaMA, Mistral.

**Open-Weight Model**
An AI model where the weights are publicly released but the training code and data may not be. Can be run locally and fine-tuned. Technically distinct from fully "open-source."

**Outpainting**
An AI technique for extending an image beyond its original borders, generating new content that naturally continues the existing image.

**Overfitting**
When a model learns the training data too well, including its noise and specific patterns, resulting in poor performance on new, unseen data.

---

## P

**Parameter**
A numerical value in a neural network that is learned during training. Modern LLMs have billions to trillions of parameters. More parameters generally (but not always) enable more capable models.

**Perplexity**
A metric for evaluating language models. Measures how well the model predicts a sequence of tokens. Lower perplexity indicates better performance.

**Pipeline**
A sequence of processing steps, often involving multiple models or tools, that transforms input into final output.

**Pre-training**
The initial, large-scale training phase of a foundation model. The model learns general language patterns from a massive text corpus using self-supervised learning.

**Prompt**
The text input given to an AI model to guide its response. Can include instructions, context, examples, and constraints.

**Prompt Engineering**
The practice of designing and optimizing prompts to effectively communicate with AI models and achieve desired outputs.

---

## Q

**Quantization**
A technique for reducing model size and memory requirements by using lower-precision numbers (e.g., 4-bit instead of 16-bit) to represent model weights. Enables running large models on consumer hardware.

**Qwen**
A family of language models developed by Alibaba Cloud. Strong multilingual performance, especially for Chinese.

---

## R

**RAG (Retrieval-Augmented Generation)**
A technique that combines information retrieval with language generation. The model first retrieves relevant documents from a database, then uses them to generate more accurate responses.

**Rate Limiting**
Restrictions on the number of API requests a user can make within a given time period. Prevents abuse and ensures fair resource distribution.

**Reasoning Model**
AI models specifically optimized for complex multi-step reasoning, such as OpenAI's o1/o3 series. These models "think" before responding, using more compute for better accuracy.

**Regression**
A machine learning task where the model predicts a continuous numerical value. Example: predicting house prices.

**Reinforcement Learning (RL)**
A machine learning paradigm where an agent learns by interacting with an environment and receiving rewards or penalties for its actions.

**Reinforcement Learning from Human Feedback (RLHF)**
A training technique where the model is optimized based on human preference rankings. Key to making LLMs helpful and aligned. Used by OpenAI, Anthropic, and others.

**RNN (Recurrent Neural Network)**
A neural network architecture designed for sequential data, where output from previous steps feeds into current processing. Largely replaced by Transformers for most tasks.

---

## S

**Sampling**
The process of selecting the next token from a probability distribution during text generation. Methods include greedy, temperature, top-k, and top-p (nucleus) sampling.

**Self-Attention**
A mechanism that allows each element in a sequence to attend to every other element, determining the relevance of each. The core innovation of the Transformer architecture.

**Self-Supervised Learning**
A training approach where the model generates its own labels from the input data. For LLMs, the task is typically predicting masked or next tokens.

**Semantic Search**
Search based on meaning rather than keyword matching. Uses embeddings and vector similarity to find semantically relevant results.

**SentencePiece**
A text tokenization library used by many models (LLaMA, Gemini). Implements BPE and unigram tokenization algorithms.

**Softmax**
A mathematical function that converts a vector of numbers into a probability distribution (values between 0 and 1 that sum to 1). Used in attention mechanisms and output layers.

**Sora**
OpenAI's video generation model that creates realistic videos from text descriptions. Uses a diffusion transformer architecture.

**Stable Diffusion**
An open-source image generation model by Stability AI. Can be run locally and is highly customizable through community extensions.

**Streaming**
A technique for delivering API responses token by token as they are generated, rather than waiting for the complete response. Improves perceived latency.

**Suno**
An AI music generation platform that creates full songs with vocals and instruments from text descriptions.

**Supervised Learning**
A machine learning paradigm where the model learns from labeled data -- input-output pairs where the correct answer is provided.

**System Prompt**
A special instruction given to an AI model that defines its behavior, personality, and constraints for the entire conversation. Set by the developer, not the end user.

---

## T

**Temperature**
A parameter that controls the randomness of AI model output. Lower temperature (0.0) produces more deterministic responses; higher temperature (1.0+) produces more creative, varied responses.

**tiktoken**
OpenAI's open-source tokenization library for Python. Used to count tokens and understand tokenization for OpenAI models.

**Token**
The basic unit of text processed by an AI model. Tokens are subword units -- typically 3-4 characters in English. Both input and output are measured in tokens.

**Tokenization**
The process of converting text into tokens (and vice versa). Different models use different tokenization schemes.

**Tokenizer**
The component that converts text to tokens (encoding) and tokens back to text (decoding). Each model family typically has its own tokenizer.

**Top-k Sampling**
A sampling strategy that restricts the model to choosing from only the k most probable next tokens.

**Top-p (Nucleus) Sampling**
A sampling strategy that restricts the model to choosing from the smallest set of tokens whose cumulative probability exceeds p.

**TPU (Tensor Processing Unit)**
Custom AI accelerator chips designed by Google, optimized for neural network computations. Used to train Google's models.

**Training Data**
The dataset used to train an AI model. For LLMs, this typically includes text from the internet, books, code, and other sources.

**Transfer Learning**
A technique where a model pre-trained on one task is adapted (fine-tuned) for a different but related task. Enables effective learning from smaller datasets.

**Transformer**
The neural network architecture introduced in the 2017 paper "Attention Is All You Need." Foundation of virtually all modern large language models and many other AI systems.

**Turing Test**
A test proposed by Alan Turing in 1950: a machine is considered intelligent if a human cannot distinguish its responses from those of another human in a text conversation.

---

## U

**Unsupervised Learning**
A machine learning paradigm where the model finds patterns in unlabeled data without explicit guidance on what to learn. Used for clustering, dimensionality reduction, and anomaly detection.

---

## V

**VAE (Variational Autoencoder)**
A generative model that learns a compressed latent representation of data and can generate new data by sampling from this space. Used in image generation pipelines.

**Vector Database**
A database optimized for storing and querying high-dimensional vector embeddings. Essential for semantic search and RAG applications. Examples: Pinecone, Weaviate, ChromaDB.

**Vision Model**
An AI model capable of understanding and processing images. Modern multimodal LLMs (GPT-4o, Claude 3+, Gemini) include vision capabilities.

**Voice Cloning**
The use of AI to replicate a person's voice from audio samples. Enables generating speech in the cloned voice saying any new text.

---

## W

**Weights**
The numerical parameters of a neural network that are learned during training. They determine how the network transforms input data into output. "Model weights" refers to all parameters collectively.

**Whisper**
OpenAI's open-source speech recognition model. Supports 99+ languages and can be run locally.

---

## Z

**Zero-Shot Learning**
The ability of a model to perform a task without any task-specific examples or training. The model relies solely on its pre-trained knowledge and the instruction provided.

---

## Acronym Quick Reference

| Acronym | Full Form |
|---|---|
| AGI | Artificial General Intelligence |
| AI | Artificial Intelligence |
| ANI | Artificial Narrow Intelligence |
| API | Application Programming Interface |
| ASI | Artificial Super Intelligence |
| BPE | Byte-Pair Encoding |
| CLIP | Contrastive Language-Image Pre-training |
| CNN | Convolutional Neural Network |
| CoT | Chain of Thought |
| DL | Deep Learning |
| GAN | Generative Adversarial Network |
| GPU | Graphics Processing Unit |
| LLM | Large Language Model |
| LoRA | Low-Rank Adaptation |
| LSTM | Long Short-Term Memory |
| ML | Machine Learning |
| MoE | Mixture of Experts |
| NLP | Natural Language Processing |
| RAG | Retrieval-Augmented Generation |
| RL | Reinforcement Learning |
| RLHF | Reinforcement Learning from Human Feedback |
| RNN | Recurrent Neural Network |
| SFT | Supervised Fine-Tuning |
| STT | Speech-to-Text |
| TPU | Tensor Processing Unit |
| TTS | Text-to-Speech |
| VAE | Variational Autoencoder |

---

*This glossary covers terms used throughout Module 01. Terms will be expanded in subsequent modules as new concepts are introduced.*
