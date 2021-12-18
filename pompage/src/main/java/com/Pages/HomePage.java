package com.Pages;

import static org.hamcrest.CoreMatchers.is;
import static org.junit.Assert.assertThat;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.interactions.Actions;
import org.openqa.selenium.support.FindBy;
import org.openqa.selenium.support.PageFactory;
import org.openqa.selenium.support.ui.ExpectedConditions;
import org.openqa.selenium.support.ui.WebDriverWait;
import org.testng.Assert;

import com.baseClass.BaseClass;
import com.baseClass.Locators;

public class HomePage extends BaseClass {
	
	@FindBy(xpath="//a[contains(text(),\'Crypto Currency\')]")
	WebElement HomeTitle;
	
	@FindBy(xpath="//a[contains(text(),'Search')]")
	WebElement Search;
	//constructor
	public HomePage(WebDriver driver) {
		this.driver=driver;
		PageFactory.initElements(driver, this);
	}
	
	public String GetTitle() 
	{
		
		return driver.getTitle();
		
	}
	
	//Home Page GetTitle and assert
    public String getHomePageTitle() {
        return driver.getTitle();
    }
    /*public void assertHomeTitle(){
      //  objConfigFileReader = new ConfigFileReader();
        assertThat(getHomePageTitle(), is(objConfigFileReader.getString("HomeTitle")));
        {
            WebDriverWait wait = new WebDriverWait(driver, 15);          
            wait.until(ExpectedConditions.presenceOfElementLocated(Locators.Home_heading_xpath1));
        }
    }*/
	
	public boolean clickOnSearch() {
		Search.click();
		//return new SearchPage();
		return true;
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
