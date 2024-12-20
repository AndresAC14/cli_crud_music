from cassandra.cluster import Cluster

# First, init Cassandra instance with Docker using:
# $ docker run --name some-cassandra -p 9042:9042 -v /path/to/datadir:/var/lib/cassandra -d cassandra:4.1

# Then, connect to the database:
cluster = Cluster(["127.0.0.1"], port=9042)
session = cluster.connect()

session.execute("CREATE KEYSPACE exam WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor': 1}")

session.execute("CREATE TABLE exam.cycling (race_year int, race_name text, PRIMARY KEY(race_year))")

# Stop here! Go to DataGrip and insert some data.

rows = session.execute('SELECT race_year, race_name FROM exam.cycling')
for row in rows:
    print(row.race_year, row.race_name)
