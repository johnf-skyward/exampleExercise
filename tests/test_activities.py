def test_get_activities_returns_activity_mapping(client):
    # Arrange
    expected_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert payload

    first_activity = next(iter(payload.values()))
    assert expected_keys.issubset(first_activity.keys())
    assert isinstance(first_activity["participants"], list)
