'''
Created on Dec 11, 2018

@author: Idan
'''


class Evaluation:
    
    def __init__(self, newsClusters):
        self.newsClusters = newsClusters
        
        self.totalAvg = 0
        self.avgSims = []
        for cluster in newsClusters.getClusters():
            avgClusterSim = self.avgClusterSimilarity(cluster) * 100
            self.totalAvg += avgClusterSim
            self.avgSims.append(avgClusterSim)
        
        self.totalAvg = self.totalAvg / len(newsClusters.getClusters())
        self.iterations = newsClusters.getIterations()
        
    
    
    
    
    
    def avgClusterSimilarity(self, cluster):
        sumSim = 0
        for point in cluster:
            sumSim += point.getSimilarity()
        return (sumSim / len(cluster))
    
    def report(self):
        print("{0} articles were assigned to {1} different clusters".format(len(self.newsClusters.getPoints()), len(self.newsClusters.getClusters())))
        print("Average similarities:")
        i = 1
        for avg in self.avgSims:
            print("Cluster #{0}: {1}".format(i, avg))
            i += 1
            
        print("Average similarities for all clusters: {0}".format(self.totalAvg))