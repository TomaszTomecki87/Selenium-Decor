from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class TestStatus(SeleniumDriver):
     __test__ = False

     log = cl.customLogger(logging.INFO)

     def __init__(self, driver):
         super().__init__(driver)
         self.resultList = []

     def setResult(self, result, resultMessage):
         try:
             if result is not None:
                 if result:
                     self.resultList.append('PASS')
                     self.log.info('### Verification Successfull ' + resultMessage)
                 else:
                    self.resultList.append('FAILED')
                    self.log.info('### Verification Failed ' + resultMessage)
                    self.screenShot(resultMessage)
             else:
                self.resultList.append('FAILED')
                self.log.info('### Verification Failed ' + resultMessage)
                self.screenShot(resultMessage)
         except:
             self.resultList.append('FAILED')
             self.log.error('### EXCEPTION!!')
             self.screenShot(resultMessage)

     def mark(self, result, resultMessage=''):
         self.setResult(result, resultMessage)

     def markFinal(self, testName, result, resultMessage=''):

         self.setResult(result, resultMessage)

         if 'FAILED' in self.resultList:
             self.log.error(testName + ' ###Test Failed')
             self.resultList.clear()
             assert True == False
         else:
             self.log.info(testName + ' ###Test Successfull')
             self.resultList.clear()
             assert True == True

