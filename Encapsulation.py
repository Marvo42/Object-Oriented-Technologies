from datetime import datetime
#Encapsulation with this we'll present the set and get methods to access privare methods and attributes of the class.
class Policy:
    def __init__(self, policy_id, status, start_date, end_date, premium: float = 0.0):
        # Private attributes
        self.__policy_id = policy_id
        self.__status = status
        self.__start_date = start_date
        self.__end_date = end_date
        self.__premium = premium

    # Getter
    def get_policy_id(self):
        return self.__policy_id

    # Setter
    def set_policy_id(self, policy_id):
        self.__policy_id = policy_id

    def get_premium(self):
        return self.__premium
    
    def update_status(self, new_status):
        self.__status = new_status

    # Determine policy type based on premium
    def get_policy_type(self):
        if self.__premium >= 10000:
            return "Family Insurance Policy"
        elif self.__premium >= 3000:
            return "Standard Insurance Policy"
        elif self.__premium >= 1500:
            return "Basic Insurance Policy"
        else:
            return "Invalid Premium Amount"

    # Display policy details
    def display_policy(self):
        return (
            f"\nPolicy ID: {self.__policy_id}"
            f"\nStatus: {self.__status}"
            f"\nStart Date: {self.__start_date}"
            f"\nEnd Date: {self.__end_date}"
            f"\nPremium: {self.__premium}"
            f"\nPolicy Type: {self.get_policy_type()}\n"
        )
class Payment:
    def __init__(self, paymentId, paymentDate, amount, policy: Policy):
        self.__paymentId = paymentId
        self.__status = "Pending"
        self.__paymentDate = paymentDate
        self.__amount = amount
        self.__policy = policy
    def processPayment(self):
        if self.__amount >= self.__policy.get_premium():
            self.__status = "Completed"
            self.__policy.update_status ("Active")
            return "Payment processed successfully."
        else:
         self.__status = "Failed"
         return "Payment failed."
    def generateReceipt(self):
        return (f"Payment ID:  {self.__paymentId}\n"
                f"Payment Date: {self.__paymentDate}\n"
                f"Amount: {self.__amount}\n"
                f"Status: {self.__status}\n"
                f"Policy ID: {self.__policy.get_policy_id()}\n")
        
class riskAssessment:
    def __init__(self, riskId, riskScore, riskLevel, policy: Policy):
        self.__riskId = riskId
        self.__riskScore = 0.0
        self.__riskLevel = "NOT YET ASSESSED"
        self.__policy = policy
        
    def evaluateRisk(self):
        premium = self.__policy.get_premium()
        if premium >= 10000.00:
            self.__riskScore = 90.0
            self.__riskLevel = "High Risk"
        elif premium >= 3000.00:
            self.__riskScore = 60.0
            self.__riskLevel = "Medium Risk"
        elif premium >= 1500.00:
            self.__riskScore = 30.0   
            self.__riskLevel = "Low Risk"          
        
        else:
            self.__riskLevel = "Invalid Premium Amount"
        return f"Risk ID: {self.__riskId}\nRisk Score: {self.__riskScore}\nRisk Level: {self.__riskLevel}\nPolicy ID: {self.__policy.get_policy_id()}\n"

#INHERITANCE & POLYMORPHISM
#This is the parent class (user) which will be inherited by child classes (Admin & Agent)
class User:
    def __init__(self, user_id, password, address, role):
        self.user_id = user_id
        self.password = password
        self.address = address
        self.role = role

    def authenticate(self):
        return (
            f"\nUser ID: {self.user_id}"
            f"\nAddress: {self.address}"
            f"\nRole: {self.role}\n"
        )

    # Polymorphic method
    def get_role(self):
        return "Normal User"


 #Child Class (Admin) Inheriting from user
class Admin(User):
    def __init__(self, user_id, password, address, admin_level):
        super().__init__(user_id, password, address, "Admin")
        self.admin_level = admin_level

    def manage_users(self):
        return f"{self.user_id} ({self.admin_level}) is managing users."

    # Polymorphism (method overriding)
    def get_role(self):
        return "System Administrator"


# Child Class (Agent) Inheriting from user
class Agent(User):
    def __init__(self, user_id, password, address, agent_role):
        super().__init__(user_id, password, address, "Agent")
        self.agent_role = agent_role

    # Association: Agent creates a Policy
    def create_policy(self, policy: Policy):
        return (
            f"{self.user_id} ({self.agent_role}) created "
            f"Policy ID: {policy.get_policy_id()}"
        )

    # Polymorphism (method overriding)
    def get_role(self):
        return "Insurance Agent"


#main
if __name__ == "__main__":

    # Create Policy
    premium_amount = float(input("Enter premium amount: "))
    policy = Policy("P12345", "Active", "2024-01-01", "2024-12-31", premium_amount)

    print(policy.display_policy())
    
    #Create Payments
    payment = Payment("Pay7566", "2023-12-11", premium_amount, policy)
    print(payment.processPayment())
    print(payment.generateReceipt())
    
    print(policy.display_policy())
    
    #Show Risk Assessment
    risk_assessment = riskAssessment("RKAs6565", 0.0, "NOT YET ASSESSED", policy)
    print(risk_assessment.evaluateRisk())
    

    # Create Users
    admin = Admin("Robert's", "rjntduhr", "Kilimani", "Group Admin")
    agent = Agent("Bruno's", "uygttde", "Nairobi West", "Sales Agent")
    admin2 = Admin("Marvin's", "djeritrbv","Buruburu 1", "Super Admin")
    agent2 = Agent("George's", "alighrikjg", "Nyari", "Sales Agent")

    print(admin.authenticate())
    print(admin.manage_users())

    print(agent.authenticate())
    print(agent.create_policy(policy))

    # Polymorphism Demo
    print("This is a Polymorphism Demonstration")
    users = [admin, agent, admin2, agent2]

    for user in users:
        print(f"{user.user_id} Role: {user.get_role()}")

        
    
        
        
   