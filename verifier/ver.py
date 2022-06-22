import pytest
import xml.etree.ElementTree as ET


LOG_PATH = "verifier/logs/test.xml"
TEST_PATH = "verifier/test_sample.py"

def parseTestXML(xmlFile=LOG_PATH):
    tree = ET.parse(xmlFile)
    root = tree.getroot()
    failure = 0
    failed_test_cases= []
    for rt in root[0]:
        test_case_name = rt.attrib['name']
        for child in rt:
            failure += 1
            failure_message = child.attrib['message']
            tmp = {'test_case_name': test_case_name, 
                    'failure_message' : failure_message}
            failed_test_cases.append(tmp)            
    return failed_test_cases


def invoke_pytest(filepath=TEST_PATH):
    pytest.main([filepath,"--junitxml", LOG_PATH]) # TODO: Replace test_path with file_path
    return parseTestXML()
    

verifier_output = invoke_pytest()


