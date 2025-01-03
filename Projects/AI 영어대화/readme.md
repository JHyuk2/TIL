# 음성 인식과 답변 제공 LLM 프로젝트

## 프로젝트 개요
이 프로젝트는 음성을 인식하고 사용자의 질문에 답변을 제공하는 경량화된 LLM(Local Language Model)을 개발하는 것을 목표로 합니다. 상업적 사용이 가능한 오픈소스 모델(MIT/Apache 라이선스)을 활용하며, Transformers 기반의 무거운 모델 대안으로 Mamba, MOE, RetNet 등의 기술을 적용하여 최적의 성능과 효율을 제공합니다.

### 찾은 모델
1. **Whisper GGUF**
   - 경량화된 음성 인식 모델.
   - 언어 지원: 다국어 (한국어 포함).
   - 다운로드: [Hugging Face - Whisper GGUF](https://huggingface.co/models?search=whisper+gguf)

   - whisper-large-v3 모델을 gguf 로 quantize
  
   1) [Whisper.cpp 설치](https://github.com/ggerganov/whisper.cpp?tab=readme-ov-file)
   > 하려고 했으나... 컴퓨터 이슈로 잠시 멈춤 ㅠ
   > 양자화된 모델을 사용하기로 변경
   
   ```bash
   git clone https://github.com/ggerganov/whisper.cpp
   cd whisper.cpp
   make
   ```



2. **LLaMA 2 GGUF**
   - Meta의 LLaMA 2 모델의 양자화 버전.
   - 텍스트 생성 및 대화에 적합.
   - 다운로드: [Hugging Face - LLaMA GGUF](https://huggingface.co/models?search=llama+gguf)

3. **Mistral GGUF**
   - 최신 경량 LLM, GGUF 지원.
   - 다운로드: [Hugging Face - Mistral GGUF](https://huggingface.co/models?search=mistral)

---

## 주요 기능
1. **음성 인식 (ASR)**:
   - 사용자의 음성을 텍스트로 변환.
   - 한국어와 영어 지원 (추후 다국어 확장).

2. **질문 답변 (QA)**:
   - 사용자의 질문을 텍스트 기반으로 분석 후 적합한 답변 생성.
3. **음성 출력 (TTS)**:
   - 텍스트로 생성된 답변을 다시 음성으로 변환하여 제공.
