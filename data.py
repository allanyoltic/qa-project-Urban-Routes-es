urban_routes_url = 'https://cnt-2990de4a-b7e9-42e6-9d74-e09e92ebdbcc.containerhub.tripleten-services.com/?lng=es'

# Derivar automáticamente la base de la API desde la URL principal
api_base_url = urban_routes_url.split('?')[0] + '/api/v1/number?number='

address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number, card_cvv = '1234 5678 9100', '111'
card_expiry = "12/30"
message_for_driver = 'Trae chocolates'