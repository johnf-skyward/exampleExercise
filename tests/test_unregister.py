from src.app import activities


def test_unregister_success_removes_participant(client):
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {"message": f"Unregistered {email} from {activity_name}"}
    assert email not in activities[activity_name]["participants"]


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Club"
    email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}


def test_unregister_non_member_returns_404(client):
    # Arrange
    activity_name = "Gym Class"
    email = "not-signed-up@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Student is not signed up for this activity"}


def test_unregister_twice_returns_404_second_time(client):
    # Arrange
    activity_name = "Gym Class"
    email = "john@mergington.edu"

    # Act
    first_response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": email}
    )
    second_response = client.delete(
        f"/activities/{activity_name}/unregister", params={"email": email}
    )

    # Assert
    assert first_response.status_code == 200
    assert second_response.status_code == 404
    assert second_response.json() == {"detail": "Student is not signed up for this activity"}
