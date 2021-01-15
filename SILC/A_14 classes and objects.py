class chair:

  def __init__(self, type, manufacturer, cost, use):
    self.type = type
    self.manufacturer = manufacturer
    self.cost = cost
    self.use = use
    
  def getDetails(self):
    print("type : " +self.type)
    print("manufacturer : " + self.manufacturer)
    print("cost : " + self.cost)
    print("use : " + self.use)

chair_1 = chair("Arm chair", "ikea", "6k", "support arms to read etc.")
chair_1.getDetails()

chair_2 = chair("desk chair", "Royaloak", "12k", "Used in offices")
chair_2.getDetails()

chair_3 = chair("folding chair", "pepperfry", "4k", "can be folded when not in use.")

chair_4 = chair("wheel chair", "knoll", "10k", "for physically handicapped")
