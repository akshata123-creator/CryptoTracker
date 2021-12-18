package com.Pages;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.PageFactory;

import com.baseClass.BaseClass;
import com.baseClass.ConfigFileReader;
import com.baseClass.Locators;
import com.baseClass.Utility;

public class DeveloperPage extends Utility {
	WebDriver driver;
	ConfigFileReader ConfigFileReader;
	Locators Locators;

	public DeveloperPage(WebDriver driver) {
		this.driver = driver;
		PageFactory.initElements(driver, this);
		objConfigFileReader = new ConfigFileReader();
		Locators = new Locators();
	}
	
	
	// ClickButton
		public void ClickButton(By elementName) {
			getWebElement(elementName).click();
		}

		// get WebElement
		public WebElement getWebElement(By elementName) {
			return driver.findElement(elementName);
		}

		// Hover mouse on the element
		public void mouseHoverOnElement(By elementName) {
			WebElement element = getWebElement(elementName);
			Actions builder = new Actions(driver);
			builder.moveToElement(element).perform();
		}

		// Assert Get Text
		public boolean AssertGetText(By elementName, String stringName) {
			//assertThat(getWebElement(elementName).getText(), is(objConfigFileReader.getString(stringName)));
			assertThat(driver.findElement(elementName).getText(), is(stringName));
			return true;
		}
}


