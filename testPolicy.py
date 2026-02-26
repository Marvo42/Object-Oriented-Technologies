from datetime import datetime

# --- CLASS DEFINITIONS ---

class Policy:
    def _init_(self, policy_id, premium_required):
        self.__policy_id = policy_id
        self.__premium_required = premium_required
        self.__status = "Pending"  # Encapsulation: Private status

    def get_premium(self):
        return self.__premium_required

    def get_id(self):
        return self.__policy_id

    def update_status(self, new_status):
        self.__status = new_status
        print(f">>> OBJECT INTERACTION: Policy {self.__policy_id} status changed to {new_status}")

    def get_details(self):
        return f"Policy: {self._policy_id} | Status: {self.status} | Premium: {self._premium_required}"


class Agent:
    def _init_(self, name):
        self.name = name

    # USE CASE 1: Issue Policy (Method call creating an object)
    def issue_policy(self, p_id, amount):
        print(f"Agent {self.name} is initiating Policy {p_id}...")
        return Policy(p_id, amount)


class Payment:
    def _init_(self, pay_id, amount_paid, policy_obj):
        self.pay_id = pay_id
        self.amount_paid = amount_paid
        self.policy = policy_obj  # Association: Payment knows about the Policy

    # USE CASE 2: Process Payment (Sequence Logic: calls methods in Policy)
    def execute_transaction(self):
        print(f"Processing Payment {self.pay_id} for Amount: {self.amount_paid}...")
        
        # Interaction: Payment calls Policy's getter
        required = self.policy.get_premium()
        
        if self.amount_paid >= required:
            # Interaction: Payment calls Policy's setter/updater
            self.policy.update_status("Active")
            return "SUCCESS: Payment Verified and Policy Activated."
        else:
            return "FAILED: Insufficient funds to activate policy."


# --- MANUAL TESTING SUITE 

if __name__ == "__main__":
   
    
    # Setup
    my_agent = Agent("Robert Mwangi")
    
    # TEST 1: Successful Issuance and Activation
    print("--- TEST CASE 01: Full Payment ---")
    test_policy_1 = my_agent.issue_policy("POL-001", 5000)
    test_payment_1 = Payment("PAY-001", 5000, test_policy_1)
    result_1 = test_payment_1.execute_transaction()
    print(f"Result: {result_1}")
    print(test_policy_1.get_details())

    # TEST 2: Underpayment (Failure logic)
    print("\n--- TEST CASE 02: Underpayment ---")
    test_policy_2 = my_agent.issue_policy("POL-002", 5000)
    test_payment_2 = Payment("PAY-002", 2000, test_policy_2)
    result_2 = test_payment_2.execute_transaction()
    print(f"Result: {result_2}")
    print(test_policy_2.get_details())