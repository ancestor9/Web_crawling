from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

'''
✅ 구현 내용
데이터베이스 없이 메모리 내 리스트(items)를 사용
REST API 기본 CRUD 기능 구현
POST /items/ → 아이템 추가
GET /items/ → 전체 아이템 조회
GET /items/{id} → 특정 아이템 조회
PUT /items/{id} → 특정 아이템 수정
DELETE /items/{id} → 특정 아이템 삭제
Swagger UI 지원 (/docs에서 직접 API 테스트 가능)
이제 FastAPI의 CRUD 개념을 쉽게 이해하고 실습할 수 있습니다! 🚀
'''



# 데이터 저장을 위한 메모리 내 리스트
items = []
item_id_counter = 1  # 아이템 ID 자동 증가

# 요청 데이터 모델
# FastAPI에서 요청 데이터의 구조를 정의하는 모델입니다.
# Pydantic 라이브러리 : 데이터의 유효성을 검사하고 관리하는 역할을 합니다.
class Item(BaseModel):
    name: str
    description: str

# 📌 Create (POST) - 아이템 추가
@app.post("/items/")
def create_item(item: Item):
    global item_id_counter
    new_item = {"id": item_id_counter, "name": item.name, "description": item.description}
    items.append(new_item)
    item_id_counter += 1
    return new_item

# 📌 Read (GET) - 모든 아이템 조회
@app.get("/items/")
def read_items():
    return items

# 📌 Read (GET) - 특정 아이템 조회
@app.get("/items/{item_id}")
def read_item(item_id: int):
    for item in items:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# 📌 Update (PUT) - 아이템 수정
@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: Item):
    for item in items:
        if item["id"] == item_id:
            item["name"] = updated_item.name
            item["description"] = updated_item.description
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# 📌 Delete (DELETE) - 아이템 삭제
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    global items
    items = [item for item in items if item["id"] != item_id]
    return {"message": "Item deleted successfully"}

# 서버 실행 방법 (터미널에서 실행)
# uvicorn yourfilename:app --reload
# 현재 디렉토리에서 yourfilename.py가 있는 지 확인하고 서버 실행하시오.


# 실습 : fake로 가상 데이터 100개를 만들어 CRUD 
