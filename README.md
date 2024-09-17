# ShillingAttack-Detection-in-Recsys
Massive amounts of useful data are constantly being generated on the internet, making it difficult for users to find information that is relevant to them. A recommendation system is a subclass of Information filtering Systems that seeks to predict the rating or the preference a user might give to an item. In simple words, it is an algorithm that suggests relevant items to users. One of the most widely used recommendation systems is collaborative filtering. However, collaborative filtering-based recommender systems open architecture makes it susceptible to shilling attacks. Shilling attacks are a type of attack in which a malicious user profile is inserted into an
existing collaborative filtering dataset to change the outcome of the recommender system. Their are two types of shilling attacks i.e. Push Attack (the attacker will give target items the highest rating) and Nuke Attack (the attacker will give target items the lowest rating). Attackers utilise user-generated data, such as user ratings and reviews, to influence recommendation ranks. Due to the widespread use of recommender systems,
more attackers are disrupting the system in an effort to profit from the altered recommendation results. So, it’s becoming more and more important
to learn how to recognise shilling attacks. To maintain their neutrality and
long-term survival, recommender systems must be able to recognise shilling
attacks. Issues with the current research include poor algorithm universality, difficulty choosing user profile attributes, and a dearth of an optimization approach. The majority of detection techniques in use today identify attackers by statistical methods. However, their detection techniques
were less effective since they were unable to detect the delicate interactions
between people and objects. In this project, we have used CoDetector, a
collaborative shilling detection model that simultaneously decomposes the
user-item interaction matrix and the user-user co-occurrence matrix with shared user latent variables.Then, the network embedding information contained in the learned user latent factors is used as a feature to identify
attackers. CoDetector outperforms state-of-the-art techniques, according
to tests done on both simulated and real-world datasets. CoDetector also
has a good performance and generalization capacity.
