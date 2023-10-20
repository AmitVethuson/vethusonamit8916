
from flask import Flask, jsonify, request

app = Flask(__name__)

students = {
        '1': {'name': 'Vethson', 'grade': 'A'},
        '2': {'name': 'Billy', 'grade': 'B'}
    }

#get all students
@app.route('/student', methods=['GET'])
def getallstudents():
    return students

#get secific student
@app.route('/student/<id>' ,methods=['GET'])
def student(id):
    if id in students:
        student_info = students.get(id, {})
        return jsonify(student_info)
    else:
        return {'error': 'student Does Not Exist'}

#create a new student
@app.route('/student',methods=['POST'])
def create_student():
    newId = (len(students)+1)
    new_student = {
        str(newId):  { 'name':request.json['name'], 'grade':request.json["grade"]}
            }
    students.update(new_student)
    return new_student

#Update student
@app.route('/student/<id>', methods=['PUT'])
def update_student(id):    
    if id in students:
        updatedStudent = {'name':request.json['name'] ,'grade': request.json['grade']}
        students.update({id:updatedStudent})
        return updatedStudent
    else:
        return {'error':'Student Not Found'}
    
    
#delete student
@app.route('/student/<id>',methods=['DELETE'])
def delete_student(id):
    if id in students:
        del students[id]
        return students
    else:
       return {'error': 'Student Does Not Exist'}




if __name__ == '__main__':
  
    app.run(debug=True)
    
