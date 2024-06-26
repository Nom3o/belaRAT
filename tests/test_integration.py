import unittest
import requests
import base64
import os
import logging

logging.basicConfig(level=logging.INFO)

class TestIntegration(unittest.TestCase):
    def test_save_snapshot(self):
        # Generate a test image
        image_path = 'test_image.png'
        with open(image_path, 'wb') as f:
            f.write(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/wcAAgAB/kaUSYoAAAAASUVORK5CYII='))

        with open(image_path, 'rb') as image_file:
            image_data = base64.b64encode(image_file.read()).decode('utf-8')
            image_data_url = f'data:image/png;base64,{image_data}'
        
        # Define the URL and payload
        url = 'http://localhost:8000/save_snapshot.php'  # Adjusted port
        payload = {
            'image': image_data_url
        }
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Basic ' + base64.b64encode(b'username:password').decode('utf-8')
        }
        
        # Send the request
        try:
            response = requests.post(url, json=payload, headers=headers)
        except requests.exceptions.RequestException as e:
            logging.error(f'Request failed: {e}')
            self.fail(f'Request failed: {e}')
        
        # Log and check the response
        logging.info(f'Response status code: {response.status_code}')
        logging.info(f'Response text: {response.text}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Snapshot saved successfully', response.text)

        # Cleanup
        os.remove(image_path)
        saved_image_path = response.text.split(': ')[1].strip()
        if os.path.exists(saved_image_path):
            os.remove(saved_image_path)

if __name__ == '__main__':
    unittest.main()
