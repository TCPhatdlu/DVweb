import uuid

from app.database import SessionLocal

from app.models import User, Document, FormulaEntry


def seed_data():
    db = SessionLocal()

    

    try:

        print("Đang tạo dữ liệu...")
        test_user = User(

            user_id=uuid.uuid4(),
            username_email="teo@dalat.edu.vn",
            password_hash="hashed_password_here",
            full_name="Lê Văn Tèo",
            role="Admin"

        )
        test_user = User(

            user_id=uuid.uuid4(),
            username_email="phat@gmail.com",
            password_hash="hashed_password_here",
            full_name="Phat",
            role="Admin2"

        )
        db.add(test_user)
        db.flush() #
        # 3. Tạo dữ liệu mẫu cho bảng Documents

        test_doc = Document(

            id=uuid.uuid4(),
            user_id=test_user.user_id,
            file_name="Giao_trinh_Toan_12.pdf",
            file_path_url="/uploads/toan12.pdf",
            status="Completed"

        )

        db.add(test_doc)

        db.flush()


        # 4. Tạo dữ liệu mẫu cho bảng FormulaEntries (Công thức LaTeX)

        formula = FormulaEntry(

            id=uuid.uuid4(),
            document_id=test_doc.id,
            latex_content=r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}",
            order_index=1

        )

        db.add(formula)
        db.commit()

        print("Tạo dữ liệu thành công! Kiểm tra pgAdmin4 để xem kết quả.")


    except Exception as e:

        print(f"Có lỗi xảy ra: {e}")
        db.rollback() 

    finally:
        db.close() 


if __name__ == "__main__":

    seed_data()