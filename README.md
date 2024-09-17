# ShillingAttack-Detection-in-Recsys
Massive amounts of useful data are constantly being generated on the internet, making it difficult for users to find information that is relevant to them. A recommendation system is a subclass of Information filtering Systems that seeks to predict the rating or the preference a user might give to an item. In simple words, it is an algorithm that suggests relevant items to users. One of the most widely used recommendation systems is collaborative filtering. However, collaborative filtering-based recommender systems open architecture makes it susceptible to shilling attacks. Shilling attacks are a type of attack in which a malicious user profile is inserted into an existing collaborative filtering dataset to change the outcome of the recommender system. Their are two types of shilling attacks i.e. Push Attack (the attacker will give target items the highest rating) and Nuke Attack (the attacker will give target items the lowest rating). Attackers utilise user-generated data, such as user ratings and reviews, to influence recommendation ranks. Due to the widespread use of recommender systems, more attackers are disrupting the system in an effort to profit from the altered recommendation results. So, it’s becoming more and more important to learn how to recognise shilling attacks. To maintain their neutrality and long-term survival, recommender systems must be able to recognise shilling attacks. Issues with the current research include poor algorithm universality, difficulty choosing user profile attributes, and a dearth of an optimization approach. The majority of detection techniques in use today identify attackers by statistical methods. However, their detection techniques were less effective since they were unable to detect the delicate interactions between people and objects. In this project, we have used CoDetector, a collaborative shilling detection model that simultaneously decomposes the user-item interaction matrix and the user-user co-occurrence matrix with shared user latent variables.Then, the network embedding information contained in the learned user latent factors is used as a feature to identify attackers. CoDetector outperforms state-of-the-art techniques, according to tests done on both simulated and real-world datasets. CoDetector also has a good performance and generalization capacity.

We have incoporated 4 common types of Shilling Attacks:

• Random Attack
Random attack also known as RandomBot attack, is the simplest form of shilling attack. Random attack model is a low knowledge attack , in which filler items (IF ) are selected in a random manner and rate them by using normal distribution
with standard deviation and mean rating of the system. In this model, the selected item set is empty i.e. (IS) = ϕ(null). The set of targeted items are rated with minimum or maximum depending on the type of attack i.e. nuke or push. For e.g.,
rating is in between 1 and 5, where 5 means liked item and 1 means disliked item, therefore, in push attack rtarget = 5 and in nuke attack, rtarget = 1. Some attacks are intended to disrupt the trustworthiness of a recommender system, known as random vandalism. Being the most straightforward attack, it is also the least effective. The purpose of a random attack is usually more effective in disrupting the performance of a Recommender System rather than promoting the target
item. The ease of execution of random attacks is because of its low-knowledge requirement. All that the attacker needs are the overall system mean which can be easily empirically calculated. Being the simplest attack, it is not very effective.

• Average Attack
Average attack model is a more sophisticated attack model than random attack model and requires knowledge of the average rating of each item in the recommender system. But it is impractical to implement because it requires knowledge about the
system, as it uses individual average ratings for each item instead of global
mean of the system. Attackers rate items in the filler set randomly using a normal
distribution with mean set to the average rating of the filler item being rated and
the standard deviation. By introducing the average attack model, attackers disguise
themselves and are harder to differentiate when compared to genuine users, thus,
have a large effect on recommendations. As with the random attack model, the
ratings of target items are set to either the maximum or minimum allowable rating
based on the intention of the attack. This attack model is considered as high
knowledge attack as it requires the average rating of individual item. However, this
attack is not much effective in case of item based algorithm.

• Bandwagon Attack
In Bandwagon attack model, attacker takes advantage of Zipf’s law distribution of
popularity and generates the biased profiles that contain most popular items.
Popular items are those items that are rated by lots of users. Therefore, there is
a high possibility that attackers become similar to the actual users. Bandwagon
attack model is the type of attack where the profiles generated by attackers
are filled with popular items with high ratings. The attack profiles are naturally
closer to a large number of users. The target item is given the highest rating.
This attack can be further divided into bandwagon-random and bandwagon-average
depending on the rating scheme used for the filler items. Bandwagon also falls under
the low-knowledge attack category since the attacker only needs publicly available
data. This attack model is considered as low knowledge attack because in order
to determine the popular products in any product space, knowledge required about
the system is less.

• Love/Hate Attack
The love/hate attack is a very simple attack, with no knowledge requirements.
Love/Hate attack model is a highly effective nuke attack. Here, the attacker randomly chooses filler items and gives them the highest ratings and the least
rating to the target item. Despite the simplicity of this model, the effectiveness is
surprisingly high. Though it was predominantly designed for nuke attacks, it can
also be used for a push attack by altering the ratings. Push attack is not as effective
as a nuke attack.
