import subprocess

# themes =["Stackoverflow","Orbit","elegant"]
themes =["Stackoverflow","flat"]

ret = subprocess.run(["node","node_modules/resume-cli/build/main.js", "export","resume/"+'abhi'+".pdf","--theme=./resume_themes/"+'my_design3',"--resume=resume/"+'abhi'+".json"], capture_output=True, text=True)  
print(ret)
print('Generating resume...')
print(ret.stdout.find("Done!"))
if ret.stdout.find("Done!") > 0:
    print('resume generated sucessfully')
else:
    print('resume generated failed')

# def generateResume(self,theme):
#     try:
#         if theme in self.themes:
#             user_id = self.request.user.id                
#             ret = subprocess.run(["node","node_modules/resume-cli/build/main.js", "export","resume/"+str(user_id)+".pdf","--theme=./resume_themes/"+theme.lower(),"--resume=resume/"+str(user_id)+".json"], capture_output=True, text=True)  
#             print(ret)  
#             if ret.stdout.find("Done!"):
#                 print("generatedResume sucess")
#             else:
#                 print("errorResume 1")
#     except Exception:
#         print("errorResume exception")