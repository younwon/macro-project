import pyautogui
import time
import keyboard # 단축키 사용을 위해 필요 (pip install keyboard)
import sys

# ==========================================
# 1. 설정 (Configuration)
# ==========================================

# 타겟 색상 (보라색, 초록색을 모두 타겟으로 설정)
TARGET_COLORS = [
    (209, 202, 249), # 보라색 (일반석)
    (176, 225, 173)  # 초록색 (OP석)
]

# 이선좌/빈좌석 색상 (현재는 참고용, 더 고도화 시 사용)
# GRAY_COLOR = (237, 239, 243) 

# 우선순위 좌석 좌표 리스트 (1순위부터 차례대로 작성)
TARGET_SEATS = [
    (1117, 499), # 1순위: OP석 (예시로 초록색을 상위 배치)
    (926, 499),  # 2순위: OP석
    (1234, 577), # 3순위
    (1235, 594),
    (1231, 616),
    (848, 578),
    (845, 598),
    (847, 615),
    (1233, 636),
    (846, 636)   # 10순위
]

# (아직 안 따셨지만) 좌석 선택 완료 버튼 좌표 - 추후 입력 필요
FINISH_BUTTON_POS = (0, 0) # 예: (1500, 800)

# 색상 오차 허용 범위 (인터파크 렌더링에 따라 색상이 미세하게 다를 수 있음)
TOLERANCE = 15

# ==========================================
# 2. 핵심 로직
# ==========================================

def color_matches(pixel_rgb, target_rgb_list, tol):
    """현재 픽셀 색상이 타겟 색상 목록 중 하나와 비슷한지 확인"""
    r, g, b = pixel_rgb
    for tr, tg, tb in target_rgb_list:
        if abs(r - tr) <= tol and abs(g - tg) <= tol and abs(b - tb) <= tol:
            return True
    return False

def hunt_seats():
    print("\n🚀 [작전 개시] 좌석 스캔을 시작합니다...")
    
    # 1. 지정된 우선순위 좌표를 순차적으로 스캔
    for i, (x, y) in enumerate(TARGET_SEATS):
        # 마우스를 해당 위치로 빠르게 이동 (사람처럼 보이게 duration 아주 살짝 추가)
        pyautogui.moveTo(x, y, duration=0.01)
        
        # 현재 위치의 픽셀 색상 확인
        current_pixel = pyautogui.pixel(x, y)
        
        # 2. 색상 판별
        if color_matches(current_pixel, TARGET_COLORS, TOLERANCE):
            print(f"🎯 [HIT!] {i+1}순위 좌석 발견! 좌표: ({x}, {y})")
            
            # 더블 클릭 (확실한 선택을 위해)
            pyautogui.click(x, y, clicks=2, interval=0.05)
            
            # 3. (중요) 이선좌 판별 또는 완료 버튼 클릭 로직
            # 실제로는 클릭 직후 '이선좌' 팝업이 뜨는지 짧게(약 0.1~0.2초) 대기하며 확인해야 함
            print("⏳ 이선좌 확인 중 (0.2초 대기)...")
            time.sleep(0.2) 
            
            # TODO: 이선좌 팝업의 '확인' 버튼 위치 색상을 확인하여 팝업이 떴는지 판단하는 로직 추가 필요
            # if 팝업 떴음:
            #     팝업 닫기 (확인 버튼 클릭 또는 Esc 키)
            #     print("💥 이선좌 발생! 다음 순위로 이동...")
            #     continue # 다음 좌석으로 넘어감
            
            # 팝업이 안 떴다면 성공으로 간주하고 완료 버튼 클릭
            print("✅ 좌석 확보 성공 (추정)! 완료 버튼 클릭 시도...")
            # pyautogui.click(FINISH_BUTTON_POS[0], FINISH_BUTTON_POS[1])
            
            # 하나 잡았으면(또는 목표 수량 달성 시) 함수 종료
            return True 
            
        else:
            print(f"⏩ {i+1}순위 ({x}, {y}) - 빈자리 아님. 다음으로 이동.")

    print("😭 모든 타겟 좌석 스캔 완료. 사용 가능한 좌석이 없습니다.")
    return False

# ==========================================
# 3. 실행 브릿지 (단축키 대기)
# ==========================================
def main():
    print("=" * 40)
    print("👾 Janus & Tesavek: 하이브리드 3.0 대기 모드 👾")
    print("=" * 40)
    print("1. 브라우저에서 티켓팅 준비를 마치세요.")
    print("2. [수동] 대기열을 뚫고 캡차(안심예매)를 입력하세요.")
    print("3. 좌석 창이 뜨는 순간 'F2' 키를 누르세요!")
    print("   (매크로를 강제 종료하려면 'Esc' 키를 누르고 유지하세요)")
    print("-" * 40)

    # F2 키를 누를 때까지 무한 대기
    keyboard.wait('f2')
    
    # F2가 눌리면 타격 로직 실행
    hunt_seats()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n중단되었습니다.")
        sys.exit()