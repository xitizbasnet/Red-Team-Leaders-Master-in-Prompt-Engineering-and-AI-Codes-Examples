# AI Model Comparison Table

## Module 01 - Foundations of Artificial Intelligence
### Comprehensive Reference Guide (Updated Early 2026)

> **Note:** The AI model landscape changes rapidly. Prices, capabilities, and model versions are updated frequently. Always verify current information on the provider's official website.

---

## 1. Large Language Models (LLMs) -- Full Comparison

### 1.1 Flagship / Frontier Models

| Feature | GPT-4o | Claude Opus 4 | Gemini 2.0 Pro | GPT-o3 |
|---|---|---|---|---|
| **Provider** | OpenAI | Anthropic | Google | OpenAI |
| **Release** | May 2024 | 2025 | Late 2024 | Early 2025 |
| **Architecture** | Transformer (MoE rumored) | Transformer | Transformer (MoE) | Transformer + CoT |
| **Context Window** | 128K tokens | 200K tokens | 1M+ tokens | 128K-200K tokens |
| **Max Output** | 16K tokens | 8K tokens | 8K tokens | 100K tokens |
| **Multimodal Input** | Text, Image, Audio | Text, Image | Text, Image, Audio, Video | Text, Image |
| **Multimodal Output** | Text, Audio | Text | Text, Image | Text |
| **Input Price/1M** | $2.50 | $15.00 | ~$1.25 | $10.00 |
| **Output Price/1M** | $10.00 | $75.00 | ~$5.00 | $40.00 |
| **Speed** | Fast | Moderate | Fast | Slow (thinks first) |
| **Reasoning** | Strong | Excellent | Strong | Excellent |
| **Coding** | Strong | Excellent | Good | Excellent |
| **Creative Writing** | Strong | Excellent | Good | Good |
| **Math** | Strong | Strong | Strong | Excellent |
| **Safety** | Moderate | Strong | Moderate | Moderate |
| **Best For** | General use, multimodal | Complex analysis, writing | Long context, multimodal | Hard reasoning, math |
| **API** | api.openai.com | api.anthropic.com | ai.google.dev | api.openai.com |

### 1.2 Mid-Tier / Balanced Models

| Feature | Claude 3.5 Sonnet | Claude Sonnet 4 | Gemini 1.5 Pro | Mistral Large |
|---|---|---|---|---|
| **Provider** | Anthropic | Anthropic | Google | Mistral AI |
| **Context Window** | 200K tokens | 200K tokens | 1M tokens | 128K tokens |
| **Input Price/1M** | $3.00 | $3.00 | $1.25 | ~$2.00 |
| **Output Price/1M** | $15.00 | $15.00 | $5.00 | ~$6.00 |
| **Speed** | Fast | Fast | Fast | Fast |
| **Reasoning** | Very Strong | Very Strong | Strong | Good |
| **Coding** | Excellent | Excellent | Good | Good |
| **Multilingual** | Good | Good | Good | Excellent |
| **Best For** | Best value for quality | Daily professional use | Long documents | European languages |

### 1.3 Fast / Cost-Effective Models

| Feature | GPT-4o mini | Claude 3.5 Haiku | Gemini 2.0 Flash | Mistral Small |
|---|---|---|---|---|
| **Provider** | OpenAI | Anthropic | Google | Mistral AI |
| **Context Window** | 128K tokens | 200K tokens | 1M tokens | 128K tokens |
| **Input Price/1M** | $0.15 | $0.80 | ~$0.075 | ~$0.20 |
| **Output Price/1M** | $0.60 | $4.00 | ~$0.30 | ~$0.60 |
| **Speed** | Very Fast | Very Fast | Very Fast | Very Fast |
| **Quality** | Good | Good | Good | Moderate |
| **Best For** | High-volume apps | Balanced fast model | Cheapest option | Budget applications |

### 1.4 Open-Weight Models

| Feature | LLaMA 3.1 405B | LLaMA 3.1 70B | Mixtral 8x22B | Qwen 2.5 72B | DeepSeek-V3 |
|---|---|---|---|---|---|
| **Provider** | Meta | Meta | Mistral AI | Alibaba | DeepSeek |
| **Parameters** | 405B | 70B | 141B (39B active) | 72B | 671B (37B active) |
| **Context Window** | 128K | 128K | 65K | 128K | 128K |
| **License** | Meta (permissive) | Meta (permissive) | Apache 2.0 | Apache 2.0 | MIT |
| **Self-Host Cost** | Very High | High | Moderate | High | Very High |
| **Via API (approx)** | ~$2-5/1M | ~$0.50-1/1M | ~$0.60-1/1M | ~$0.50-1/1M | $0.27/$1.10 |
| **Reasoning** | Strong | Good | Good | Good | Strong |
| **Coding** | Strong | Good | Good | Strong | Strong |
| **Multilingual** | Good | Good | Good | Excellent (Chinese) | Good (Chinese) |
| **Can Fine-Tune** | Yes | Yes | Yes | Yes | Yes |
| **Can Run Locally** | No (too large) | Yes (80GB+ VRAM) | Yes (48GB+ VRAM) | Yes (80GB+ VRAM) | No (too large) |
| **Best For** | Max open perf | Self-hosted LLM | Efficient inference | Chinese + multilingual | Cost-effective API |

---

## 2. Image Generation Models

| Feature | DALL-E 3 | Midjourney v6 | Stable Diffusion XL | Flux.1 Pro | Ideogram 2.0 |
|---|---|---|---|---|---|
| **Provider** | OpenAI | Midjourney Inc. | Stability AI | Black Forest Labs | Ideogram AI |
| **Type** | Closed | Closed | Open Source | Semi-Open | Closed |
| **Max Resolution** | 1024x1792 | 2048x2048 | 1024x1024 | 2048x2048 | 2048x2048 |
| **Text in Images** | Good | Moderate | Poor | Good | Excellent |
| **Photorealism** | Good | Excellent | Good | Very Good | Good |
| **Artistic Quality** | Good | Excellent | Good (customizable) | Very Good | Good |
| **Prompt Adherence** | Excellent | Good | Good | Very Good | Very Good |
| **Run Locally** | No | No | Yes | Yes (Schnell/Dev) | No |
| **Customizable** | No | No | Very (LoRA, CN) | Moderate | No |
| **Price per Image** | $0.04-0.08 | ~$0.03-0.10 | Free (local) | ~$0.04-0.06 | $0.02-0.08 |
| **Best For** | Prompt following | Aesthetics | Customization | Quality + text | Text rendering |

---

## 3. Audio / Speech Models

### 3.1 Text-to-Speech (TTS)

| Feature | ElevenLabs | OpenAI TTS | Azure Neural TTS | XTTS (Open Source) |
|---|---|---|---|---|
| **Quality** | Excellent | Good | Very Good | Good |
| **Voice Cloning** | Yes | No | Yes (custom) | Yes |
| **Languages** | 29+ | 50+ | 140+ | 16+ |
| **Voices Available** | 1000s + custom | 6 preset | 400+ | Community |
| **Emotion Control** | Yes | Limited | Yes (SSML) | Limited |
| **Price** | $5-330/month | $15-30/1M chars | Pay per char | Free |
| **Run Locally** | No | No | No | Yes |
| **Latency** | Low | Low | Low | Medium |
| **Best For** | Content creation | Simple integration | Enterprise | Privacy/self-host |

### 3.2 Speech-to-Text (STT)

| Feature | Whisper (OpenAI) | Deepgram | AssemblyAI | Azure STT |
|---|---|---|---|---|
| **Type** | Open Source | Cloud API | Cloud API | Cloud API |
| **Languages** | 99+ | 36+ | 100+ | 100+ |
| **Real-time** | No (batch) | Yes | Yes | Yes |
| **Diarization** | No (natively) | Yes | Yes | Yes |
| **Accuracy** | Excellent | Excellent | Excellent | Very Good |
| **Run Locally** | Yes | No | No | No |
| **Price** | Free (local) | ~$0.0043/min | ~$0.006/min | ~$0.01/min |
| **Best For** | Local/research | Real-time apps | Content analysis | Enterprise |

### 3.3 Music Generation

| Feature | Suno | Udio | MusicGen (Meta) | Stable Audio |
|---|---|---|---|---|
| **Vocals** | Yes | Yes | No | Limited |
| **Instrumental** | Yes | Yes | Yes | Yes |
| **Max Duration** | 4 min | 2 min | 30 sec | 3 min |
| **Custom Lyrics** | Yes | Yes | No | No |
| **Genres** | All | All | Most | Most |
| **Quality** | Excellent | Excellent | Good | Good |
| **Open Source** | No | No | Yes | No |
| **Price** | Free-$30/mo | Free-$30/mo | Free | Free-$20/mo |
| **Commercial Use** | Pro plan+ | Pro plan+ | Research license | Pro plan+ |
| **Best For** | Full songs | Full songs | Instrumentals | Background music |

---

## 4. Video Generation Models

| Feature | Sora | Runway Gen-3 | Pika | Kling | Luma Dream Machine |
|---|---|---|---|---|---|
| **Provider** | OpenAI | Runway ML | Pika Labs | Kuaishou | Luma AI |
| **Max Duration** | ~20s | 10s (extend) | 10s | 120s | 5s (extend) |
| **Max Resolution** | 1080p | 1080p | 1080p | 1080p | 720p-1080p |
| **Text-to-Video** | Yes | Yes | Yes | Yes | Yes |
| **Image-to-Video** | Yes | Yes | Yes | Yes | Yes |
| **Camera Control** | Basic | Excellent | Basic | Good | Basic |
| **Physics** | Very Good | Good | Fair | Good | Fair |
| **Consistency** | Very Good | Good | Fair | Good | Fair |
| **Special Effects** | No | Limited | Yes (fun) | Limited | No |
| **Lip Sync** | No | No | Yes | No | No |
| **Speed** | Slow | Moderate | Fast | Moderate | Fast |
| **Price Range** | $$$ (sub) | $12-76/mo | $8-58/mo | Free-$28/mo | Free/sub |
| **API Access** | Limited | Yes | Limited | Yes | Yes |
| **Best For** | Quality | Pro control | Social media | Long videos | Quick prototypes |

---

## 5. Coding AI Models / Tools

| Feature | Claude Code | GitHub Copilot | Cursor | GPT-4o (coding) | DeepSeek Coder |
|---|---|---|---|---|---|
| **Provider** | Anthropic | GitHub/OpenAI | Cursor Inc. | OpenAI | DeepSeek |
| **Type** | CLI Agent | IDE Extension | Full IDE | API | Open Source |
| **Model** | Claude Sonnet/Opus | GPT-4o / Claude | Multiple (switchable) | GPT-4o | DeepSeek-Coder |
| **Agentic** | Yes (full) | Limited | Yes | Via API | No |
| **Code Generation** | Excellent | Very Good | Very Good | Strong | Strong |
| **Code Editing** | Excellent | Good | Very Good | Via API | Good |
| **Multi-file** | Yes | Limited | Yes | Manual | No |
| **Debugging** | Excellent | Good | Good | Good | Good |
| **Price** | Usage-based | $10-39/mo | $20-40/mo | API pricing | Free/cheap API |
| **Best For** | Complex projects | Daily coding | AI-first IDE | API integration | Budget coding |

---

## 6. Quick Selection Guide

### By Use Case

| Use Case | Recommended Model | Why |
|---|---|---|
| General chat and Q&A | GPT-4o mini or Claude Haiku | Fast, cheap, good enough |
| Complex analysis | Claude 3.5 Sonnet | Best reasoning at mid-tier price |
| Coding | Claude Sonnet or GPT-4o | Top coding performance |
| Long document processing | Gemini 1.5 Pro | 1M token context window |
| Math and science | o3 or Claude Opus | Best reasoning capabilities |
| Creative writing | Claude Opus or GPT-4o | Nuanced, creative output |
| Translation | Gemini or Mistral Large | Strong multilingual support |
| High-volume, low-cost | GPT-4o mini | $0.15/$0.60 per 1M tokens |
| Data privacy | LLaMA 3.1 (self-hosted) | Data never leaves your infra |
| Image generation | Midjourney for art, DALL-E for accuracy | Each has unique strengths |
| Music generation | Suno | Best overall quality with vocals |
| Video generation | Sora for quality, Runway for control | Depends on needs |
| Voice synthesis | ElevenLabs | Most natural-sounding voices |
| Transcription | Whisper (local) or Deepgram (API) | Free vs. real-time |

### By Budget

| Monthly Budget | Recommended Stack |
|---|---|
| **Free** | Whisper (local) + HuggingFace models + free tiers of Suno/Pika |
| **Under $20** | ChatGPT Plus or Claude Pro for personal use |
| **$20-100** | API access (GPT-4o mini or Claude Haiku for volume) |
| **$100-500** | Mix of Claude Sonnet + GPT-4o mini + image/audio tools |
| **$500-2,000** | Full API access to frontier models for professional use |
| **$2,000+** | Enterprise plans, self-hosted models, multi-provider strategy |

---

## 7. Benchmark Performance (Approximate Rankings)

> These rankings are approximate and based on available benchmarks as of early 2026. Performance varies by specific task.

### Overall Intelligence (MMLU, GPQA, etc.)
1. GPT-o3 / Claude Opus 4
2. GPT-4o / Claude 3.5 Sonnet
3. Gemini 2.0 Pro / DeepSeek-V3
4. LLaMA 3.1 405B / Qwen 2.5 72B
5. Mistral Large / Mixtral 8x22B

### Coding (HumanEval, SWE-bench)
1. Claude Opus 4 / Claude Sonnet 4
2. GPT-o3 / GPT-4o
3. DeepSeek-Coder-V3
4. Gemini 2.0 Pro
5. LLaMA 3.1 405B / Qwen 2.5-Coder

### Instruction Following (IFEval, MT-Bench)
1. Claude 3.5 Sonnet / Claude Sonnet 4
2. GPT-4o
3. Gemini 2.0 Pro
4. Mistral Large
5. LLaMA 3.1 70B

### Speed (Tokens per Second, API)
1. Groq (LLaMA on LPU) -- 500+ tok/s
2. Gemini Flash -- 300+ tok/s
3. GPT-4o mini -- 200+ tok/s
4. Claude Haiku -- 150+ tok/s
5. Claude Sonnet -- 100+ tok/s

---

*Last updated: February 2026*
*Prices and capabilities change frequently -- always verify with official sources.*
