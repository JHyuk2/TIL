import streamlit as st
from PIL import Image, ImageEnhance
from filters import apply_grayscale
from streamlit_drawable_canvas import st_canvas
from inpaintings import load_inpainting_pipeline, run_inpainting

# streamlit 제목 및 설명
st.title("AI-Powered Image Editor")
st.write("Upload an image and apply a grayscale filter!")

# 이미지 업로드
uploaded_file = st.file_uploader("choose an image", type=["jpg", "jpeg", "png"])

# 모델 로드
st.write("Loading the inpainting model...")
pipeline = load_inpainting_pipeline()
st.success("Model loaded successfully!")

# 업로드된 이미지 표시
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # 캔버스 설정
    st.write("Draw the area to be masked:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 255, 255, 1)", # 채우기 색상(흰색)
        stroke_width=5, # 선 굵기
        stroke_color="rgba(0, 0, 0, 1)", # 선 색상(검정색)
        background_image=image, #캔버스 배경으로 업로드된 이미지 사용
        update_streamlit=True,
        height=image.size[1],
        width=image.size[0],
        drawing_mode="freedraw", # 자유 선택 도구
        key="canvas"
    )

    if canvas_result.image_date is not None:
        # 캔버스를 마스크로 변환
        mask = image.fromarray((canvas_result.image_data[:, :, 3]>0).astype("unit8")*255)
        st.image(mask, caption="Generated Mask", use_container_width=True)

        # Inpainting 실행
        prompt = st.text_input("Enter a prompt for inpainting:", "Fill this area naturally.")
        if st.button("Run inpainting"):
            with st.spinner("Inpainting in progress..."):
                result = run_inpainting(pipeline, image, mask, prompt)
            st.image(result, caption="Inpainting Result", use_container_width=True)


    """
    # 밝기 조절 슬라이더
    if st.button("Adjust Brightness"):
        brightness = st.slider("Adjust Brightness", min_value=0.1, max_value=2.0)
        enhanced_image = ImageEnhance.Brightness(image).enhance(brightness)
        st.image(enhanced_image, caption="Brightness Adjusted Image", use_container_width=True)
    

    # 흑백 필터 적용 버튼
    if st.button("Apply Grayscale Filter"):
        grayscale_image = apply_grayscale(image)
        st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)
    """
