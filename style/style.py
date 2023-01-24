# Стиль для виджетов.
STYLE_CENTRAL_WIDGET = ("""
                        #centralWidget{
                          background-color: #d9d9d9;
                        }
                        """)
STYLE_ACTION_WIDGET = ("""
                       #actionWidget{
                         background-color: white;
                         border-radius: 10px;
                       }
                       """)
STYLE_PARAMETERS_WIDGET = ("""
                           #parametersWidget{
                             background-color: white;
                             border-radius: 10px;
                           }
                           """)

# Стиль для кнопок.
STYLE_PUSH_BUTTON_CLEAR = ("""
                           #pushButtonClear{
                             background-color: rgba(0, 0, 0, 0);
                             border-radius: 10px;
                             font-size: 20px;
                             font-family: bold "Times New Roman";
                           }
                           #pushButtonClear::hover{
                             background-color: #e3e3e3;
                           }
                           #pushButtonClear::pressed{
                             background-color: #c9f5ff;
                           }
                           """)
STYLE_PUSH_BUTTON_RESULT = ("""
                            #pushButtonResult{
                              background-color: rgba(0, 0, 0, 0);
                              border-radius: 10px;
                              font-size: 20px;
                              font-family: bold "Times New Roman";
                            }
                            #pushButtonResult::hover{
                              background-color: #e3e3e3;
                            }
                            #pushButtonResult::pressed{
                              background-color: #c9f5ff;
                            }
                            """)
STYLE_PUSH_BUTTON_SAVE = ("""
                          #pushButtonSave{
                            background-color: rgba(0, 0, 0, 0);
                            border-radius: 10px;
                            font-size: 20px;
                            font-family: bold "Times New Roman";
                          }
                          #pushButtonSave::hover{
                            background-color: #e3e3e3;
                          }
                          #pushButtonSave::pressed{
                            background-color: #c9f5ff;
                          }
                          """)
STYLE_PUSH_BUTTON_EXIT = ("""
                          #pushButtonExit{
                            background-color: rgba(0, 0, 0, 0);
                            border-radius: 10px;
                            font-size: 20px;
                            font-family: bold "Times New Roman";
                          }
                          #pushButtonExit::hover{
                            background-color: #e3e3e3;
                          }
                          #pushButtonExit::pressed{
                            background-color: #c9f5ff;
                          }
                          """)
STYLE_PUSH_BUTTON_EDIT_DATABASE = ("""
                                   #pushButtonEditDatabase{
                                     background-color: rgba(0, 0, 0, 0);
                                     border-radius: 5px;
                                     image: url(./icons/edit.png);
                                     font-size: 20px;
                                     font-family: bold "Times New Roman";
                                   }
                                   #pushButtonEditDatabase::hover{
                                     background-color: #f7f7f7;
                                   }
                                   #pushButtonEditDatabase::pressed{
                                     background-color: #c9f5ff;
                                   }
                                   """)

# Стиль для полей изменения текста.
STYLE_LINE_EDIT_DATABASE = ("""
                            #lineEditDatabase{
                              font-size: 14px;
                              font-family: bold "Times New Roman";
                              border: 1px solid #ced4da;
                              border-radius: 10px;
                              padding-left: 5px;
                              padding-right: 5px;
                            }
                            """)

# Стиль для текста.
STYLE_LABEL_MATERIAL = ("""
                        #labelMaterial{
                          font-size: 15px;
                          font-family: bold "Times New Roman";
                        }
                        """)

STYLE_LABEL_EDIT_DATABASE = ("""
                             #labelEditDatabase{
                               font-size: 15px;
                               font-family: bold "Times New Roman";
                             }
                             """)
STYLE_LABEL_BRAND = ("""
                     #labelBrand{
                       font-size: 15px;
                       font-family: bold "Times New Roman";
                     }
                     """)
STYLE_LABEL_TYPE_PART = ("""
                         #labelTypePart{
                           font-size: 15px;
                           font-family: bold "Times New Roman";
                         }
                         """)
STYLE_LABEL_NAME_PART = ("""
                         #labelNamePart{
                           font-size: 15px;
                           font-family: bold "Times New Roman";
                         }
                         """)

# Стиль для комбинированных кнопок.
STYLE_COMBO_BOX_MATERIAL = ("""
                            #comboBoxMaterial{
                              border: 1px solid #ced4da;
                              border-radius: 10px;
                              padding-left: 5px;
                              font-size: 14px;
                              font-family: bold "Times New Roman";
                            }
                            #comboBoxMaterial::drop-down{
                              border: 0px;
                            }
                            #comboBoxMaterial::down-arrow{
                              image: url(./icons/down_arrow.png);
                              width: 20px;
                              height: 20px;
                              margin-right: 8px;
                            }
                            #comboBoxMaterial::on{
                              border: 4px solid #e5e5e5;
                            }
                            #comboBoxMaterial QListView{
                              font-size: 12px;
                              border: 1px solid rgba(0, 0, 0, 10%);
                              padding: 5px;
                              background-color: #fff;
                              outline: 0px;
                            }
                            #comboBoxMaterial QListView::item{
                              padding-left: 10px;
                              background-color: #fff;
                            }
                            #comboBoxMaterial QListView::item:hover{
                              background-color: #1e90ff;
                            }
                            #comboBoxMaterial QListView::item:selected{
                              background-color: #1e90ff;
                            }
                            """)
STYLE_COMBO_BOX_BRAND = ("""
                         #comboBoxBrand{
                           border: 1px solid #ced4da;
                           border-radius: 10px;
                           padding-left: 5px;
                           font-size: 14px;
                           font-family: bold "Times New Roman";
                         }
                         #comboBoxBrand::drop-down{
                           border: 0px;
                         }
                         #comboBoxBrand::down-arrow{
                           image: url(./icons/down_arrow.png);
                           width: 20px;
                           height: 20px;
                           margin-right: 8px;
                         }
                         #comboBoxBrand::on{
                           border: 4px solid #e5e5e5;
                         }
                         #comboBoxBrand QListView{
                           font-size: 12px;
                           border: 1px solid rgba(0, 0, 0, 10%);
                           padding: 5px;
                           background-color: #fff;
                           outline: 0px;
                         }
                         #comboBoxBrand QListView::item{
                           padding-left: 10px;
                           background-color: #fff;
                         }
                         #comboBoxBrand QListView::item:hover{
                           background-color: #1e90ff;
                         }
                         #comboBoxBrand QListView::item:selected{
                           background-color: #1e90ff;
                         }
                         """)
STYLE_COMBO_BOX_TYPE_PART = ("""
                             #comboBoxTypePart{
                               border: 1px solid #ced4da;
                               border-radius: 10px;
                               padding-left: 5px;
                               font-size: 14px;
                               font-family: bold "Times New Roman";
                             }
                             #comboBoxTypePart::drop-down{
                               border: 0px;;
                             }
                             #comboBoxTypePart::down-arrow{
                               image: url(./icons/down_arrow.png);
                               width: 20px;
                               height: 20px;
                               margin-right: 8px;
                             }
                             #comboBoxTypePart::on{
                               border: 4px solid #e5e5e5;
                             }
                             #comboBoxTypePart QListView{
                               font-size: 12px;
                               border: 1px solid rgba(0, 0, 0, 10%);
                               padding: 5px;
                               background-color: #fff;
                               outline: 0px;
                             }
                             #comboBoxTypePart QListView::item{
                               padding-left: 10px;
                               background-color: #fff;
                             }
                             #comboBoxTypePart QListView::item:hover{
                               background-color: #1e90ff;
                             }
                             #comboBoxTypePart QListView::item:selected{
                               background-color: #1e90ff;
                             }
                             """)
