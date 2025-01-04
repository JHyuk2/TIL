# 음성 인식과 답변 제공 LLM 프로젝트



## 프로젝트 개요

이 프로젝트는 음성을 인식하고 사용자의 질문에 답변을 제공하는 경량화된 LLM(Local Language Model)을 개발하는 것을 목표로 합니다. 상업적 사용이 가능한 오픈소스 모델(MIT/Apache 라이선스)을 활용하며, Transformers 기반의 무거운 모델 대안으로 Mamba, MOE, RetNet 등의 기술을 적용하여 최적의 성능과 효율을 제공합니다.



### 음성 인식(ASR: Automatic Speech Recognition) 모델

1. **Whisper**
   
   [Whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo)
   
- 경량화된 음성 인식 모델.
  
  - 언어 지원: 다국어 (한국어 포함).
  
     > large-v3, large-turbo만 다국어 지원, 그 외에는 english only
  
   1) 필요한 라이브러리 설치
  
   ```bash
   pip install --upgrade pip
   pip install --upgrade transformers datasets[audio] accelerate
   ```
  
  
  
   2) `pipeline` 사용하기
  
  ```python
  import torch
  from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
  from datasets import load_dataset
  
  
  device = "cuda:0" if torch.cuda.is_available() else "cpu"
  torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
  
  model_id = "openai/whisper-large-v3-turbo"
  
  model = AutoModelForSpeechSeq2Seq.from_pretrained(
      model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
  )
  model.to(device)
  
  processor = AutoProcessor.from_pretrained(model_id)
  
  pipe = pipeline(
      "automatic-speech-recognition",
      model=model,
      tokenizer=processor.tokenizer,
      feature_extractor=processor.feature_extractor,
      torch_dtype=torch_dtype,
      device=device,
  )
  
  dataset = load_dataset("distil-whisper/librispeech_long", "clean", split="validation")
  sample = dataset[0]["audio"]
  
  result = pipe(sample)
  print(result["text"])
  
  ```
  
  
  
   3)
  
   4)
  
   5)





1. **LLaMA 2 GGUF**

   - Meta의 LLaMA 2 모델의 양자화 버전.
   - 텍스트 생성 및 대화에 적합.
   - 다운로드: [Hugging Face - LLaMA GGUF](https://huggingface.co/models?search=llama+gguf)

   > LLaMa2  모델 자체가 오래된 버전이다 보니, 다른 모델을 먼저 찾아볼 것 같다.

   

2. **Mistral GGUF**

   - 최신 경량 LLM, GGUF 지원.
   - 다운로드: [Hugging Face - Mistral GGUF](https://huggingface.co/models?search=mistral)

   

3. **DeepSeek V3** 

   - MoE기반의 최신 LLM(12/30/2024), GGUF사용...

     ~~사용을 시도 했으나...4비트 양자화된 모델마저 400기가가 넘어 사용불가...~~

---

## 주요 기능
1. **음성 인식 (ASR)**:
   - 사용자의 음성을 텍스트로 변환.
   - 한국어와 영어 지원 (추후 다국어 확장).

2. **질문 답변 (QA)**:
   - 사용자의 질문을 텍스트 기반으로 분석 후 적합한 답변 생성.
3. **음성 출력 (TTS)**:
   - 텍스트로 생성된 답변을 다시 음성으로 변환하여 제공.
