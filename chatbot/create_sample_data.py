"""
Sample test data for the alumni chatbot.
This file creates a sample CSV file for testing the chatbot.
"""

import pandas as pd
import os

def create_sample_alumni_csv(filepath='sample_alumni.csv'):
    """Create a sample alumni database CSV for testing"""
    
    data = {
        'Name': [
            'Rajesh Kumar', 'Priya Sharma', 'Amit Patel', 'Neha Singh', 'Arjun Gupta',
            'Divya Verma', 'Rohit Desai', 'Anjali Nair', 'Vikram Reddy', 'Sakshi Jain',
            'Nikhil Rao', 'Pooja Kapoor', 'Aditya Mishra', 'Riya Malhotra', 'Sanjay Kumar',
            'Deepika Iyer', 'Harshit Singh', 'Medha Patil', 'Gaurav Dubey', 'Shreya Chopra'
        ],
        'Year': [
            2015, 2016, 2017, 2018, 2019,
            2016, 2017, 2018, 2019, 2020,
            2015, 2016, 2017, 2018, 2019,
            2016, 2017, 2018, 2019, 2020
        ],
        'Branch': [
            'CSE', 'ECE', 'CSE', 'ME', 'EEE',
            'CSE', 'ECE', 'CSE', 'ME', 'EEE',
            'CSE', 'ECE', 'CSE', 'ME', 'EEE',
            'CSE', 'ECE', 'CSE', 'ME', 'EEE'
        ],
        'Company': [
            'Google', 'Microsoft', 'Google', 'Amazon', 'Apple',
            'Facebook', 'Google', 'Microsoft', 'Amazon', 'Google',
            'Microsoft', 'Apple', 'Google', 'Amazon', 'Facebook',
            'Google', 'Microsoft', 'Amazon', 'Apple', 'Google'
        ],
        'Position': [
            'Software Engineer', 'Data Scientist', 'Senior Engineer', 'Product Manager', 'DevOps Engineer',
            'Frontend Engineer', 'Backend Engineer', 'ML Engineer', 'QA Engineer', 'Software Engineer',
            'Data Engineer', 'Security Engineer', 'Cloud Architect', 'SRE', 'Full Stack Engineer',
            'Solutions Architect', 'Product Manager', 'Engineering Manager', 'Research Scientist', 'Tech Lead'
        ],
        'Location': [
            'Bangalore', 'Seattle', 'Mountain View', 'Seattle', 'Cupertino',
            'Menlo Park', 'Bangalore', 'Redmond', 'Bangalore', 'Mountain View',
            'Bangalore', 'Cupertino', 'Mountain View', 'Seattle', 'Menlo Park',
            'Bangalore', 'Redmond', 'Seattle', 'Cupertino', 'Mountain View'
        ],
        'Skills': [
            'Python, Java, C++', 'Python, R, SQL', 'Java, Spring, Docker', 'Leadership, Product Design',
            'Linux, AWS, Docker', 'JavaScript, React, Node.js', 'Java, Spring, SQL', 'TensorFlow, Python, Keras',
            'Selenium, Java, Python', 'Python, Java, Git', 'Python, Spark, Hadoop', 'Security, Networking, Linux',
            'Kubernetes, AWS, Terraform', 'Monitoring, Incident Management', 'JavaScript, Python, React',
            'AWS, Azure, Cloud Architecture', 'Product Strategy, Analytics', 'Team Management, Engineering',
            'Machine Learning, Research', 'Technical Leadership, Architecture'
        ]
    }
    
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Sample CSV created: {filepath}")
    return filepath

if __name__ == '__main__':
    sample_file = create_sample_alumni_csv()
    print(f"\nCreated sample file: {sample_file}")
    print("\nTo use this file:")
    print("1. Run: python app.py")
    print("2. Upload the sample_alumni.csv file through the web interface")
    print("3. Start querying!")
