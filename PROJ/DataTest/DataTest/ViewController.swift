//
//  ViewController.swift
//  DataTest
//
//  Created by Kedan Li on 15/9/30.
//  Copyright © 2015年 TakeFive Interactive. All rights reserved.
//

import Cocoa

class ViewController: NSViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        DataManager.parseBids()

        // Do any additional setup after loading the view.
    }

    override var representedObject: AnyObject? {
        didSet {
        // Update the view, if already loaded.
        }
    }


}

