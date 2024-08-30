import unittest
from .. import create_app
from ..config.config import config_dict
from ..models.orders import Order
from..models.users import User
from ..utils.db import db
from flask_jwt_extended import create_access_token


class OrderTestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(config=config_dict['test'])
        
        self.appctx=self.app.app_context()

        self.appctx.push()

        self.client=self.app.test_client()

        db.create_all()


        # Create a test user
        self.test_user = User(username='testuser', email='testuser@company.com', password_hash='password')
        db.session.add(self.test_user)
        db.session.commit()

    def tearDown(self):
        db.drop_all()

        self.app=None

        self.appctx.pop()


        self.client =None


    def test_get_all_orders(self):
        
        token=create_access_token(identity='testuser')

        headers={
            "Authorization":f"Bearer {token}"
        }
        response=self.client.get('/orders/orders/',headers=headers)

        assert response.status_code == 200

        assert response.json == []

    def test_create_order(self):
        

        data={
            "size":"LARGE",
            "quantity":3,
            "flavour": "Test flavour"
        }

        token=create_access_token(identity='testuser')

        headers={
            "Authorization":f"Bearer {token}"
        }

        response=self.client.post('/orders/orders/',json=data, headers=headers)

        assert response.status_code == 201


        orders= Order.query.all()

        assert len(orders) == 1

    def test_get_order(self):
        pass

    def test_update_order(self):
        pass

    def test_delete_order(self):
        pass