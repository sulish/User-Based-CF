import pandas as pd, numpy as np, matplotlib.pyplot as plt,time
from sklearn import metrics
from sklearn.cluster import DBSCAN
from geopy.distance import great_circle
from shapely.geometry import MultiPoint


df = pd.read_csv('train1.csv')
coords = df.as_matrix(columns=['lat', 'lng'])


kms_per_radian = 6371.0088
epsilon = 0.55 / kms_per_radian
start_time = time.time()
db = DBSCAN(eps=epsilon, min_samples=500, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
cluster_labels = db.labels_
num_clusters = len(set(cluster_labels))

# print cluster_labels

# message = 'Clustered {:,} points down to {:,} clusters, for {:.1f}% compression in {:,.2f} seconds'

# print(message.format(len(df), num_clusters, 100*(1 - float(num_clusters) / len(df)), time.time()-start_time))

# print('Silhouette coefficient: {:0.03f}'.format(metrics.silhouette_score(coords, cluster_labels)))

a = np.matrix(cluster_labels)
a_list = list(a.flat)
with open('train1.csv', 'r') as f:
  i = 0;
  for row in f:
    if 'checkin' not in row:
      if '\n' in row:
        form = str(row.replace('\n',''))+','+str(a_list[i])
      else:
        form = str(row)+','+str(a_list[i])

      # print form

      output = open("dbscan-train1-0.55,500.csv","a")
      output.write(form+'\n')
      output.close()
      i+=1



clusters = pd.Series([coords[cluster_labels == n] for n in range(num_clusters)])
print('Number of clusters: {}'.format(num_clusters))

def get_centermost_point(cluster):
    centroid = (MultiPoint(cluster).centroid.x, MultiPoint(cluster).centroid.y)
    centermost_point = min(cluster, key=lambda point: great_circle(point, centroid).m)
    return tuple(centermost_point)

centermost_points = clusters.map(get_centermost_point)

lats, lons = zip(*centermost_points)
rep_points = pd.DataFrame({'lng':lons, 'lat':lats})

rs = rep_points.apply(lambda row: df[(df['lat']==row['lat']) & (df['lng']==row['lng'])].iloc[0], axis=1)

fig, ax = plt.subplots(figsize=[10, 6])
rs_scatter = ax.scatter(rs['lng'], rs['lat'], c='#99cc99', edgecolor='None', alpha=0.7, s=120)
df_scatter = ax.scatter(df['lng'], df['lat'], c='k', alpha=0.9, s=3)
ax.set_title('Full data set vs DBSCAN reduced set')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend([df_scatter, rs_scatter], ['Full set', 'Reduced set'], loc='upper right')
plt.show()