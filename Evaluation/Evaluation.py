'''

@author: Idan
'''
import Utilities
import os

#    Class Evaluation    #

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
        self.dissim = self.calcAvgClustersDissim()
        
    
    
    #This method calculates the average similarity within a cluster
    def avgClusterSimilarity(self, cluster):
        sumSim = 0
        for point in cluster:
            sumSim += point.getSimilarity()
        return (sumSim / len(cluster))
    
    #This method calculates the average dissimilarity between clusters
    def calcAvgClustersDissim(self):
        centroids = self.newsClusters.getCentroids()
        result = []
        for i in range(len(centroids)):
            for j in range(i+1, len(centroids)):
                dissim = (1 - Utilities.cosineSimilarity(centroids[i], centroids[j])) * 100
                result.append(dissim)
        avg = sum(result) / len(result)
        return avg
    
    #This method creates output files of clustering results
    def createResult(self):
        statPath = os.path.dirname(os.path.abspath(__file__)) + "\Stats.txt"
        clustersPath = os.path.dirname(os.path.abspath(__file__)) + "\Clusters.txt"
        
        #Writing to statistics file
        with open(statPath, 'w') as output:
            output.write("{0} articles were assigned to {1} different clusters within {2} iterations\n".format(len(self.newsClusters.getPoints()), len(self.newsClusters.getClusters()), self.iterations))
            output.write("Average similarities:\n")
            i = 1
            for avg in self.avgSims:
                output.write("Cluster #{0}: {1} %\n".format(i, "%.2f" % avg))
                i += 1
            output.write("Average similarities for all clusters: {0} %\n".format("%.2f" % self.totalAvg))
            output.write("Average dissimilarities between clusters: {0} %\n ".format("%.2f" % self.dissim))

        #Writing to clusters file
        with open(clustersPath, 'w') as output:
            i = 1
            for cluster in self.newsClusters.getClusters():
                output.write('Cluster #{0}\n'.format(i))
                for point in cluster:
                    output.write(str(point))
                    output.write("\n")
                output.write("\n")
                i += 1