

# 1. Успешный тест шаблона "Order Form":
echo "=== Test Order Form ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"user_name":"example","user_email":"example@example.com","order_date":"2022-12-01"}' \
  http://localhost:8000/get_form
echo -e "\n"

# 3. Успешный тест шаблона "Lead Form":
echo "=== Test Lead Form ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"lead_email":"example@example.com","lead_phone":"+79999999999"}' \
  http://localhost:8000/get_form
echo -e "\n"

# 4. Успешный тест шаблона "Basic Form":
echo "=== Test Basic Form ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"contact_info":"Any text here"}' \
  http://localhost:8000/get_form
echo -e "\n"

# 5. Тест 1 ответа не подходящего под существующие формы
echo "=== Test No Matching Template 1 ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"some_field":"some_value","lead_phone":"+79999999999", "user_email": "example@example.com"}' \
  http://localhost:8000/get_form
echo -e "\n"

# 6. Тест 2 ответа не подходящего под существующие формы
echo "=== Test No Matching Template 2 ==="
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"order_date": "08.12.2024"}' \
  http://localhost:8000/get_form
echo -e "\n"
