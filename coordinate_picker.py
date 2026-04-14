import pyautogui
import sys
import time

def main():
    print("=" * 40)
    print("🎯 하이브리드 작전: 좌표 및 색상 추출기 🎯")
    print("=" * 40)
    print("1. 예매 연습 페이지를 띄우고 좌석 위로 마우스를 올리세요.")
    print("2. 터미널 창을 선택한 상태에서 'Enter' 키를 누르면 현재 마우스 위치의 정보가 저장됩니다.")
    print("3. 'q'를 입력하고 Enter를 누르면 종료됩니다.\n")

    saved_points = []

    try:
        while True:
            # 사용자의 입력을 대기합니다.
            user_input = input("Enter를 눌러 좌표 저장 (종료: q): ")
            
            if user_input.lower() == 'q':
                break

            # 현재 마우스 위치와 해당 픽셀의 RGB 값을 가져옵니다.
            x, y = pyautogui.position()
            pixel_color = pyautogui.pixel(x, y)
            
            point_info = {"x": x, "y": y, "color": pixel_color}
            saved_points.append(point_info)
            
            print(f"✅ 저장됨: 좌표(X:{x}, Y:{y}) | 색상(RGB): {pixel_color}")
            print("-" * 30)

    except KeyboardInterrupt:
        pass

    print("\n" + "=" * 40)
    print("🎉 추출 완료! 저장된 목록입니다:")
    print("=" * 40)
    
    # 파이썬 리스트 형태로 바로 복사할 수 있게 출력합니다.
    print("SEAT_COORDINATES = [")
    for pt in saved_points:
        print(f"    ({pt['x']}, {pt['y']}),")
    print("]")
    
    if saved_points:
        print("\n감지된 색상 목록 (가장 많이 나온 색상을 TARGET_COLOR로 사용하세요):")
        colors = [pt['color'] for pt in saved_points]
        for color in set(colors):
            print(f"- {color} (빈도: {colors.count(color)})")

if __name__ == "__main__":
    # 라이브러리 확인을 위한 간단한 예외 처리
    try:
        import pyautogui
    except ImportError:
        print("pyautogui 라이브러리가 설치되지 않았습니다.")
        print("터미널에 'pip install pyautogui'를 입력하여 설치해주세요.")
        sys.exit(1)
        
    main()