from fastapi.testclient import TestClient

from src import app as app_module


client = TestClient(app_module.app)


def test_student_cannot_sign_up_twice_for_same_activity():
    activity_name = "Chess Club"
    email = "newstudent@mergington.edu"

    first_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )
    assert first_response.status_code == 200

    second_response = client.post(
        f"/activities/{activity_name}/signup?email={email}"
    )

    assert second_response.status_code == 400
    assert "already signed up" in second_response.text.lower()
