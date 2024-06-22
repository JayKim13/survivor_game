def 물_마시기():
  print("무인도의 물이 오염된 것 같습니다.")
  print("간이 정수기를 만들어야 할 것 같습니다.")
  print("지금 눈에 보이는 것 중 정수기에 필요한 재료를 3개 골라보자.")

  materials = ["1:PT병", "2:자갈", "3:비닐", "4:모래", "5:타이어", "6:캔","7:공","8:책","9:판"]
  print("눈에 보이는 것은:", ", ".join(materials))

  while True:
      selected_materials = input("숫자 3개를 콤마로 구분해서 번호를 입력하세요: ").split(',')
      selected_materials = [material.strip() for material in selected_materials]

      if len(selected_materials) != 3:
          print("3개의 재료를 숫자로 정확히 입력해 주세요.")
          continue

      if "1" in selected_materials and "2" in selected_materials and "4" in selected_materials:
          print("이제 필요한 것은 다 구했으니, 간이 정수기를 만들어 보자")
          break
      else:
          print("다시 고르세요.")

  print("PT병을 칼로 반으로 나누고 아래 그림처럼 놓아보자")
  print("  |-----|")
  print("  |_   _| ")
  print("    | |   ")
  print("  |     |")
  print("  |_____|")
  print("혼합물을 분리할때 돌의 크기를 이용했었습니다.")
  print("PT병 주둥이가 있는 부분에 자갈과 모래를 넣어야하는데...어떤 순서로 넣어야 할까요?")
  print("단 세개의 재료를 모두 사용해야 합니다.")
  print("1:자갈, 2:모래,3:천")
  while True:
      heart = 4
      윗부분 = input("윗부분에 넣을 것을 입력하세요: ").strip()
      중간 = input("중간 부분에 넣을 것을 입력하세요: ").strip()
      아래 = input("아래에 넣을 것을 입력하세요: ").strip()

      if   윗부분 == "1"and 중간== "2" and 아래=="3":
          print("드디어 정수기 완성됐어. 주변에 물이 있으면 정수기에 넣어서 마십시오")
          break
      else:
          print("앗! 물을 부어봤더니 계속 흙탕물입니다. 다시 시도하세요.")
          heart -= 1
          if heart <= 1:
              print("게임 오버")
              print(r"""
              ------------
              |  YOU DIED |
              ------------
              """)
              break



def 사냥_시도():
  print("사냥을 하다가 위험한 동물과 마주쳤습니다.")
  animals = ["살모사", "호랑이", "곰", "독거미", "독화살 개구리", "코브라", "악어", "정체를 모르는 어떤 생명체"]
  print("동물과 싸우시겠습니까?\n1.예\n2.아니오")
  fight = input("선택: ")
  animal = random.choice(animals)

  if fight == "1":
      print(f"당신은 {animal}와 싸우기로 결정하였습니다. 당신의 선택!")
      print("1. 기권한다.")
      print("2. 서둘러 뒤에 무기가 있는지 살펴본다.")
      print("3. 맨손으로 싸운다.")
      decision = input("선택: ")

      if decision == "1":
          print(f"{animal}가 당신을 쫓아가 다리를 깨물었습니다. \n결과적으로 당신은 한쪽 다리를 잃게 되었고 과다 출혈로 사망하였습니다.")
          print("게임 오버")
          print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
          time.sleep(2)
          return False

      elif decision == "2":
          print("당신은 작은 철 조각을 찾았습니다. 동물에게 이 것을 던지시겠습니까?")
          print("1. 예")
          print("2. 아니오")
          weapon = input("선택: ")

          if weapon == "1":
              print("당신은 기적적으로 방어에 성공하여 동물을 물리쳤습니다. 축하드립니다! 사냥을 계속 하시겠습니까?")
              print("1. 예")
              print("2. 아니오")
              continue_hunt = input("선택: ")

              if continue_hunt == "1":
                  print("이 곳에는 사냥꾼과 밀렵꾼들이 많아 사냥을 하려면 다음 퀴즈를 풀어야 합니다.")
                  print("Q. 생태계에서 생산자는 무엇을 의미합니까?")
                  print("1. 죽은 동물을 먹는 생물")
                  print("2. 식물을 먹는 동물")
                  print("3. 태양 에너지를 이용해 유기물을 만드는 생물")
                  print("4. 다른 동물을 먹는 동물")
                  answer = input("선택: ").strip()

                  if answer == "3":
                      print("정답입니다. 고기를 얻고 캠프로 안전하게 돌아갑니다.")
                      print(r"""
  -----------------------
  |  CONGRATULATIONS!    |
  |  You have succeeded! |
  -----------------------
      """)
                  else:
                      print("오답입니다. 사냥에 실패하여 빈손으로 캠프로 돌아갑니다.")
                      print(r"""
  --------------
  |  YOU FAILED |
  --------------
      """)
              else:
                  print("캠프로 안전하게 돌아갑니다.")
                  print(r"""
  ------------------
  |  SAFE RETURN   |
  ------------------
      """)

          else:
              print(f"당신의 망설임으로 {animal}가 분노했지만, 결국 도망칩니다.")
              print("캠프로 안전하게 돌아갔지만, 아무것도 얻지 못했습니다.")
              print(r"""
  ------------------
  |  SAFE RETURN   |
  ------------------
      """)

      elif decision == "3":
          print("당신은 맨손으로 싸우기로 결심했습니다.")
          print("퀴즈를 푸십시오.")
          print("Q. 숲에서 동물들이 먹이를 찾기 어려운 계절은 언제인가요?")
          print("1. 봄")
          print("2. 여름")
          print("3. 가을")
          print("4. 겨울")
          hunting_answer = input("선택: ").strip()

          if hunting_answer == "4":
              print(f"정답입니다. 당신은 기적적으로 {animal}를 물리쳤습니다. 고기를 모아 캠프로 돌아가시겠습니까?\n1. 예\n2. 아니오")
              hunting_choice = input("선택: ").strip()
              if hunting_choice == "1":
                  print("당신은 사냥을 계속합니다. 하지만 이 곳에는 사냥꾼과 밀렵꾼들이 많아 사냥을 하려면 다음 퀴즈를 풀어야 합니다.")
                  print("Q. 생태계에서 분해자의 역할은 무엇인가요?")
                  print("1. 빛 에너지를 이용해 유기물을 만든다.")
                  print("2. 죽은 생물의 유해를 분해하여 무기질로 되돌린다.")
                  print("3. 다른 동물을 잡아먹는다.")
                  print("4. 다른 생물의 기생충을 제거한다.")
                  hunting = input("선택: ").strip()

                  if hunting == "2":
                      print("정답입니다.")
                      print("퀴즈에 성공하여 사냥을 할 수 있게 되었습니다. 생존에 한 걸음 더 다가섰습니다.")
                      print("식량과 자원을 가지고 캠프로 돌아갑니다.")
                      print(r"""
  -----------------------
  |  CONGRATULATIONS!   |
  |  You have succeeded!|
  -----------------------
      """)
                  else:
                      print("퀴즈에 실패하여 사냥에 실패하였습니다. 빈손으로 캠프로 돌아갑니다.")
                      print("얼마 후 당신은 배고픔으로 죽었습니다.")
                      print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
                      time.sleep(2)
                      return False
              else:
                  print("캠프로 안전하게 돌아갑니다.")
                  print(r"""
  ------------------
  |  SAFE RETURN    |
  ------------------
      """)
          else:
              print(f"실패하였습니다.{animal}에게 제압당해 심각한 부상을 입었습니다. 상처로 인해 사망하였습니다. 게임 오버.")
              print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
              time.sleep(2)
              return False

  else:
      print(f"{animal}와 마주쳤지만 싸우지 않기로 했습니다. 안전하게 도망쳤지만 캠프로 빈손으로 돌아갑니다.")
      print("얼마 후 당신은 배고픔으로 죽었습니다.")
      print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
      time.sleep(2)
      return False

def 불_피우기_시도():
  print("\n불을 피우기 위해서는 나무를 찾아서 장작을 만들어야 합니다.")
  time.sleep(0.5)
  print("장작을 만드려면, 오랜 시간이 걸릴지라도, 도끼부터 만들어야 합니다.")
  choice_firewood_a = int(input("도끼를 만드시겠습니까? Yes=1, No=2: "))
  if choice_firewood_a == 1:
      # 도끼 만들기
      time.sleep(2.5)
      print("\n도끼 날로 사용할 돌을 찾았습니다.")
      time.sleep(1)
      print("날을 갈 도구를 모으는 중입니다. 잠시 기다려 주세요.")
      time.sleep(4)
      print("여러 도구를 모았습니다. 어떤 도구를 사용할까요? 도구 선택에 실패할 경우 죽게 되니 신중히 결정해 주세요.")
      tools = ["돌", "나무", "조개껍데기", "동물의 뼈"]

      for index, tool in enumerate(tools):
          print(f"{index + 1}: {tool}")

      try:
          user_choice = int(input("도구 번호를 선택하세요: ")) - 1
          selected_tool = tools[user_choice]

          if user_choice == 0:
              print("\n돌로 날을 갈았습니다. 결과는 아주 성공적이었습니다.")
          elif user_choice == 1:
              print("나무로 날을 갈려고 했지만 나무가 갈려 실패했습니다.")
              print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
              return False
          elif user_choice == 2:
              print("조개껍데기로 날을 갈았습니다. 결과는 나쁘지 않았습니다.")
          elif user_choice == 3:
              print("동물의 뼈 중 아무거나 갈아 보았습니다. 하지만 뼈가 쪼개져 버렸습니다.")
              print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
              return False
      except (ValueError, IndexError):
          print("잘못된 도구를 선택하셨습니다. 1에서 4 사이의 숫자를 입력하세요.")
          return False

      print("도끼가 완성되었습니다.")
      time.sleep(0.5)
      print("\n도끼로 나무를 잘라서 장작을 만들 때까지 기다려주세요.")
      time.sleep(6)
      print("장작을 다 만들었습니다.")

      # 불을 피우기
      time.sleep(2)
      print("\n바다 바람으로 인하여 추워졌습니다. 장작에 불을 피워야 합니다.")
      print("바닷물에 떠다니던 라이터를 주워서 장작에 불을 붙이기를 시도했으나, 장작에 불이 붙기 전에 라이터의 연료가 떨어져서 실패하였습니다.")
      time.sleep(0.5)
      print("\n퀴즈를 맞추고 다른 도구로 불을 피워보세요.")
      fire_quiz_1 = ["인화점", "착화점", "쌍화점"]

      for index, tool in enumerate(fire_quiz_1):
          print(f"{index + 1}: {tool}")

      try:
          user_choice = int(input("이 보기 중 물체가 불의 힘을 빌리지 않고 연소할 수 있는 온도는? (숫자를 입력하세요): ")) - 1
          if user_choice == 0:
              print("틀렸습니다.\n해당 단어는 물체가 불의 도움으로 타기 시작하는 온도로, 나무의 인화점은 250°C 입니다.")
              time.sleep(1)
              print("불을 붙이지 못하고 당신은 저체온증으로 사망했습니다.")
              print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
              return False
          elif user_choice == 2:
              print("틀렸습니다. 해당 단어는 영화 제목이자 중국집 이름입니다.")
              time.sleep(1)
              print("불을 붙이지 못하고 당신은 저체온증으로 사망했습니다.")
              print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
              return False
          elif user_choice == 1:
              print("\n정답을 맞췄습니다.")
              print("이번에는 불을 붙이기 위해 필요한 물건을 모두 맞춰보세요.")
              fire_quiz_2 = ["장작", "토치", "유리병", "물"]

              for index, tool in enumerate(fire_quiz_2):
                  print(f"{index + 1}: {tool}")

              while True:
                  selected_materials = input("숫자 2개를 콤마로 구분해서 번호를 입력하세요: ").split(',')
                  selected_materials = [material.strip() for material in selected_materials]
                  if len(selected_materials) != 2:
                      print("2개의 재료를 숫자로 정확히 입력해 주세요.")
                      continue
                  if "1" in selected_materials and "2" in selected_materials:
                      print("\n정답을 맞췄습니다.")
                      time.sleep(1)
                      print("\n토치만 있으면 불을 피울 수 있지만 토치가 없습니다.\n토치 대신 빛의 굴절을 이용해 돋보기로 장작에 불을 붙이려고 합니다. 시도하는 중...")
                      time.sleep(5)
                      fire_quiz_3 = int(input("하지만, 장작의 착화점이 너무 높아 불이 붙지 않습니다.\n주변에 종이 무더기가 보입니다. 종이는 장작보다 착화점이 낮습니다. \n게다가 일반적으로 물체의 착화점보다 인화점이 더 낮습니다. \n장작보다 종이에 먼저 불을 붙여보시겠습니까? 예=1, 아니오=2: "))
                      if fire_quiz_3 == 1:
                          print("다행히도 종이에 불이 붙었습니다. \n곧바로 불붙은 종이 위에 장작을 올리고, 불이 꺼지지 않도록 추가 종이를 계속 공급해 주었습니다.")
                          time.sleep(0.5)
                          print("그리하여 장작의 온도가 인화점까지 올라갔습니다.")
                          time.sleep(0.5)
                          print("드디어 장작에 불을 붙이는 것을 성공하였습니다. 축하합니다.")
                          time.sleep(1)
                          fire_quiz_4 = int(input("\n좀 쉬고 있는데 목이 마릅니다. 물을 마시러 가시겠습니까? 예=1, 아니오=2: "))
                          if fire_quiz_4 == 1:
                              print("물 마시기 코너로 이동합니다.")
                              물_마시기()
                          elif fire_quiz_4 == 2:
                              print("물을 마시지 않고 당신은 갈증으로 사망했습니다.")
                              print(r"""
  ------------
  |  YOU DIED |
  ------------
""")
                              return False
                      elif fire_quiz_3 == 2:
                          print("불을 붙이지 못하고 당신은 저체온증으로 사망했습니다.")
                          print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
                          return False
                  else:
                      print("틀렸습니다. 정답은 장작,토치입니다.")
                      return False
      except (ValueError, IndexError):
          print("잘못된 도구를 선택하셔서 사망하셨습니다.")
          print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
          return False
  else:
      print("도끼를 만들지 않기로 결정했습니다.")
      time.sleep(0.5)
      print("얼마 뒤 당신은 저체온증으로 사망했습니다.")
      print(r"""
  ------------
  |  YOU DIED |
  ------------
      """)
      return False


print("당신은 무인도에 홀로 남겨졌습니다.")
print("비행기가 추락한 후 유일하게 살아남은 당신은 외딴 섬에 고립되었습니다.")
print("주변을 둘러보니 바다와 정글, 그리고 야생 동물들로 가득합니다.")
print("생존을 위해 여러 가지 행동을 해야 합니다.")
print("주의: 행동을 선택할 때 항상 유효한 옵션을 선택하세요.")

print("행동을 선택하세요:")
print("1. 물 마시기")
print("2. 사냥하기")
print("3. 불 피우기")
while True:
  선택 = input("선택지 번호를 입력하세요: ")

  if 선택 == '1':
      물_마시기()
  elif 선택 == '2':
      if not 사냥_시도():
          break
  elif 선택 == '3':
      if not 불_피우기_시도():
          break
  else:
      print("올바른 선택지 번호를 입력하세요.")

  더_할_건지 = input("한개를 더해야 무인도에서 살아남을 수 있습니다. 다른 행동을 선택하시겠습니까? (예/아니오): ")
  if 더_할_건지.strip() != '예':
      break
