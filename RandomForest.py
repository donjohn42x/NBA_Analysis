# Build the model
 
h2o.init()
Train_h2o<-as.h2o(Full_df)
 
Train_h2o$H_Outcome<-as.factor(Train_h2o$H_Outcome)
 
# random forest model
model1 <- h2o.randomForest(y = 16, x=c(4:15), training_frame = Train_h2o, max_depth=4 )
 
h2o.performance(model1)