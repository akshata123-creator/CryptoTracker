package com.Pages;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;
import static org.testng.Assert.assertTrue;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.CacheLookup;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;

import com.baseClass.BaseClass;
import com.baseClass.ConfigFileReader;
import com.baseClass.Locators;
import com.baseClass.Utility;

public class SearchPage extends Utility {
	WebDriver driver;
	ConfigFileReader ConfigFileReader;
	Locators Locators;
	@FindBy(id = "email")
	@CacheLookup
	public WebElement Email;
	
	
	
	//constructor
		public SearchPage(WebDriver driver) {
			this.driver = driver;
			PageFactory.initElements(driver, this);
		    objConfigFileReader = new ConfigFileReader();
		    Locators=new Locators();
		}
		
		// set email
		public void setEmail(String Email1) {
			Email.sendKeys(Email1);
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
		public void AssertGetText(By elementName, String stringName) {
			assertThat(driver.findElement(elementName).getText(), is(stringName));
		}

			// editable textbox
		public void fieldEditable(By elementName) {
			WebElement element = driver.findElement(elementName);
			Boolean isEditable = element.isEnabled() && element.getAttribute("readonly") == null;
			assertTrue(isEditable);
		}


}
