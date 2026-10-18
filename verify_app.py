from cliff_project.app import app
client = app.test_client()
r = client.post('/', data={'income': '1500', 'raise': '100'})
print('status_code', r.status_code)
print('has_status_div', '<div id="status">' in r.get_data(as_text=True))
print('has_snapshot', 'SNAP Status: SAFE' in r.get_data(as_text=True))
print(r.get_data(as_text=True)[:500])
