class RecommendationStrategy:

  def calculate(self,strategy,p,q):
    #try:
      #emptyThing = []
      n = 0
      modifiedP = []
      modifiedQ = []
      for item in p:
        if len(q) >= (n + 1):
          n += 1
          if (type(item) == type(q[n - 1])):
            if (item >= 0 and q[n-1] >= 0):
              modifiedP += [item]
              modifiedQ += [q[n-1]]

      return strategy.strategy(modifiedP,modifiedQ)
    #except:
      return "Interface not implemented properly"