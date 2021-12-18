package com.baseClass;

import java.io.File;

import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.BeforeSuite;

import com.aventstack.extentreports.ExtentReports;
import com.aventstack.extentreports.ExtentTest;
import com.aventstack.extentreports.reporter.ExtentSparkReporter;

public class Utility  {
	WebDriver driver;
	
	public ConfigFileReader objConfigFileReader;
	public ExtentSparkReporter htmlReporter;
	public ExtentReports extent;
	public ExtentTest test1;
	//public ExtentTest test2;
	

	
	public WebDriver setup() {
		System.setProperty("webdriver.chrome.driver","C:\\ChromeDriver\\chromedriver.exe");
		WebDriver driver= new ChromeDriver();
		driver.manage().window().maximize();
		objConfigFileReader = new ConfigFileReader();
		return driver;
	}
	
	

}
