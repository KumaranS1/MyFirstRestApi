from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#dict to hold data
accounts = {}

class CreateAccount(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=str, required=True)
        parser.add_argument('initial_balance', type=float, default=0)
        args = parser.parse_args()
        account_id = args['account_id']
        if account_id in accounts:
            return {'message': 'Account already exists'}, 400
        accounts[account_id] = args['initial_balance']
        return {'message': 'Account created successfully', 'account_id': account_id}, 201

class Account(Resource):
    def get(self, account_id):
        if account_id not in accounts:
            return {'message': 'Account does not exist'}, 404
        return {'account_id': account_id, 'balance': accounts[account_id]}, 200

class Deposit(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=str, required=True)
        parser.add_argument('amount', type=float, required=True)
        args = parser.parse_args()
        account_id = args['account_id']
        if account_id not in accounts:
            return {'message': 'Account does not exist'}, 404
        accounts[account_id] += args['amount']
        return {'message': 'Deposit successful', 'account_id': account_id, 'new_balance': accounts[account_id]}, 200

class Withdraw(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=str, required=True)
        parser.add_argument('amount', type=float, required=True)
        args = parser.parse_args()
        account_id = args['account_id']
        if account_id not in accounts:
            return {'message': 'Account does not exist'}, 404
        if accounts[account_id] < args['amount']:
            return {'message': 'Insufficient balance'}, 400
        accounts[account_id] -= args['amount']
        return {'message': 'Withdrawal successful', 'account_id': account_id, 'new_balance': accounts[account_id]}, 200

api.add_resource(CreateAccount, '/create_account')
api.add_resource(Account, '/account/<string:account_id>')
api.add_resource(Deposit, '/deposit')
api.add_resource(Withdraw, '/withdraw')

if __name__ == '__main__':
    app.run(debug=True)