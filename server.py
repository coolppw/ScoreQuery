import grpc
import time
from concurrent import futures
import mysql.connector
import query_pb2_grpc
import query_pb2

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
_HOST = 'localhost'
_PORT = '6060'

class queryScore(query_pb2_grpc.queryScoreServicer):

    def queryDatebase(self, id, lesson):
        mydb = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            passwd='123456',
            db='scores',
            charset='utf8'
        )
        cur = mydb.cursor()
        print(lesson)
        if lesson == 'Java':
            cur.execute('select * from Java')
        elif lesson == 'C':
            cur.execute('select * from C')
        data = cur.fetchall()
        res = '0'
        for i in data :
            if i[0] == id :
                res = i[2]
                break
        cur.close()
        mydb.close()
        return res

    def query(self, request, context):
        id = request.id
        name = request.name
        lesson = request.lesson
        grade = self.queryDatebase(id, lesson)
        print("query function called")
        return query_pb2.queryResponse(score = grade)

def serve():
    grpcServer = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    print("Begin")
    query_pb2_grpc.add_queryScoreServicer_to_server(queryScore(), grpcServer)
    grpcServer.add_insecure_port(_HOST + ':' + _PORT)
    grpcServer.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        grpcServer.stop(0)

if __name__ == '__main__':
    serve()